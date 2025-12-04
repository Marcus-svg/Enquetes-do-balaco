from abc import ABC, abstractmethod

class printOne:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(printOne, cls).__new__(cls)
            cls._instance.line = []
        return cls._instance

    def add_document(self, document):
        print(f" Documento recebido na fila >> {document[:15]}...")
        self.line.append(document)

    def print_all(self):
        print("\n--- INICIANDO IMPRESSÃO ---")
        if not self.line:
            print("Fila vazia.")
        for test, doc in enumerate(self.line, 1):
            print(f"Imprimindo Doc {test}:\n{doc}\n{'-'*30}")
        self.line = []

class ReportDraft:
    def __init__(self):
        self.title = ""
        self.paragraph = []
        self.baseboard = ""

class ReportBuilder:
    def __init__(self):
        self.draft = ReportDraft()

    def set_title(self, text):
        self.draft.title = text
        return self

    def add_paragraph(self, text):
        self.draft.paragraph.append(text)
        return self

    def set_baseboard(self, text):
        self.draft.baseboard = text
        return self

    def build(self):
        return self.draft

class Exporter(ABC):
    @abstractmethod
    def exporter(self, draft: ReportDraft):
        pass

class exporterHTML(Exporter):
    def exporter(self, draft):
        html = f"<html>\n<h1>{draft.title}</h1>\n<body>"
        for p in draft.paragraph:
            html += f"\n  <p>{p}</p>"
        html += f"\n  <footer>{draft.baseboard}</footer>\n</body>\n</html>"
        return html

class exporterTXT(Exporter):
    def exporter(self, draft):
        txt = f"=== {draft.title.upper()} ===\n\n"
        for p in draft.paragraph:
            txt += f"{p}\n"
        txt += f"\n--- {draft.baseboard} ---"
        return txt

class exporterFactory:
    def create_exporter(shape):
        if shape == "html":
            return exporterHTML()
        elif shape == "txt":
            return exporterTXT()
        else:
            print(f"Formato '{shape}' não suportado. Usando TXT padrão.")
            return exporterTXT()

if __name__ == "__main__":
    print("=== SISTEMA GERADOR DE RELATÓRIOS TG_CIA_LTA ===\n")

    report_data = (ReportBuilder()
                       .set_title("Relatório Mensal de Vendas")
                       .add_paragraph("O faturamento subiu 22% em relação a outubro.")
                       .add_paragraph("O produto mais vendido foi o 'Botijão P13'.")
                       .add_paragraph("A meta para o próximo mês é dobrar a meta.")
                       .set_baseboard("Tião do gás e cia")
                       .build())

    shape_chosen = "html"
    
    exporter = exporterFactory.create_exporter(shape_chosen)

    final_document = exporter.exporter(report_data)

    spooler = printOne()
    spooler.add_document(final_document)

    spooler.add_document("Lembrete: Reunião às 09h.")

    spooler.print_all()