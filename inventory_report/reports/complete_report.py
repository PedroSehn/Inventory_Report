from inventory_report.reports.ReportTools.oldest_fabrication import (
    oldest_fabrication,
)
from inventory_report.reports.ReportTools.sooner_expiration import (
    sooner_expiration,
)
from inventory_report.reports.ReportTools.most_items import most_items
from inventory_report.reports.ReportTools.items_per_company import (
    items_per_company,
)
from inventory_report.reports.ReportTools.stringfy_items import stringfy_items


class CompleteReport:
    def generate(list):
        companies_dict = items_per_company(list)
        string_list = stringfy_items(companies_dict)
        return (
            f"Data de fabricação mais antiga: {oldest_fabrication(list)}\n"
            f"Data de validade mais próxima: {sooner_expiration(list)}\n"
            f"Empresa com mais produtos: {most_items(list)}\n"
            f"Produtos estocados por empresa:\n"
            f"{string_list}"
        )


CompleteReport.generate = staticmethod(CompleteReport.generate)
