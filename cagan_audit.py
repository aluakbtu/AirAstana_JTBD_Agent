import os
import sys
import pypdf
import google.generativeai as genai
from colorama import init, Fore, Style

init(autoreset=True)

API_KEY = "My_API_KEY" 
PDF_PATH = r'C:\Users\Acer\OneDrive\Документы\TSIS1. JTBD Interviewer Agent\annual-report-2024.pdf'
COMPANY_NAME = "Air Astana Group"

SYSTEM_PROMPT = f"""
### ANALYSIS FRAMEWORK (THE "CAGAN TEST")
Analyze the uploaded documents for evidence of the following. Quote specific page numbers or financial figures where possible.

1. MERCENARIES vs. MISSIONARIES:
   - Do they talk about "delivering requirements from the business" (Mercenaries)?
   - Or do they talk about "solving customer problems" and "outcomes" (Missionaries)?

2. PROJECT vs. PRODUCT FUNDING:
   - Is there evidence of "annual budgeting cycles" for specific projects (Project mindset)?
   - Or is there "continuous funding" for persistent teams (Product mindset)?

3. IT vs. PRODUCT:
   - Is "IT" treated as a cost center or a back-office support function?
   - Is there a separation between "The Business" and "Technology"? (In a product model, they are one).

4. OUTPUT vs. OUTCOME:
   - Do they measure success by "features shipped" or "on-time delivery"?
   - Or do they measure business results (retention, revenue per user, engagement)?

### INSTRUCTIONS
1.  **Ingest:** Read the provided documents thoroughly.
2.  **Diagnose:** Compare the text against the ANALYSIS FRAMEWORK above.
3.  **Draft:** Generate a "Transformation Memo" addressed to the Board of Directors.

### FORMAT: THE TRANSFORMATION MEMO
The output must be a professional 1-page memo using the following structure:

**TO:** Board of Directors, {COMPANY_NAME}
**FROM:** External Product Transformation Auditor
**DATE:** 2026-02-02
**SUBJECT:** Diagnostic of Product Operating Model Maturity

**1. EXECUTIVE SUMMARY**
[1-2 sentences summarizing if the company is "Digital Native" or "Digital Immigrant" based on the text.]

**2. EVIDENCE OF "FEATURE FACTORY" BEHAVIOR (RISKS)**
[List 3 specific quotes or data points from the Annual Report that indicate an old-school IT mindset. Explain WHY this is a risk according to Cagan.]

**3. STRATEGIC DISCONNECTS**
[Identify where the company says they want "Innovation" but their financial allocation suggests "Maintenance".]

**4. THE PRESCRIPTION**
[3 bullet points on how they must shift from Project-based management to Product-based management.]

### CONSTRAINTS
- Do not generalize. If the document doesn't say it, say "Insufficient Evidence."
- Be critical but professional.
- Use the terminology of Marty Cagan (e.g., "Empowered Teams," "Product Discovery")
"""

class CaganAuditAgent:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model_name = self._get_available_model()
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction=SYSTEM_PROMPT
        )

    def _get_available_model(self):
        try:
            available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            for pref in ['models/gemini-2.5-flash', 'models/gemini-1.5-flash', 'models/gemini-pro']:
                if pref in available: return pref
            return available[0]
        except: return "gemini-pro"

    def extract_pdf_text(self, path):
        print(Fore.YELLOW + f"[*] Читаю ВЕСЬ документ: {path}")
        try:
            reader = pypdf.PdfReader(path)
            text = ""
            for i, page in enumerate(reader.pages):
                content = page.extract_text()
                if content:
                    # Добавляем метку страницы для точности цитирования
                    text += f"\n[DOCUMENT PAGE {i+1}]\n{content}"
            print(Fore.GREEN + f"[+] Успешно извлечено {len(reader.pages)} страниц.")
            return text
        except Exception as e:
            print(Fore.RED + f"[-] Ошибка PDF: {e}"); sys.exit(1)

    def run_full_analysis(self, document_text):
        print(Fore.CYAN + "[*] Запуск полного анализа (весь текст отправлен в ИИ)...")
        prompt = f"Analyze the following full report for {COMPANY_NAME}:\n\n{document_text}"
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(Fore.RED + f"[-] Ошибка анализа: {e}"); sys.exit(1)

    def save_result(self, content):
        filename = f"Full_Cagan_Audit_{COMPANY_NAME.replace(' ', '_')}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(Fore.GREEN + f"\n[SUCCESS] Полный аудит сохранен в: {filename}")

def main():
    agent = CaganAuditAgent(API_KEY)
    full_text = agent.extract_pdf_text(PDF_PATH)
    memo = agent.run_full_analysis(full_text)
    agent.save_result(memo)

if __name__ == "__main__":
    main()