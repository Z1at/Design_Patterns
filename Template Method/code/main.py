class ReportGenerator:  # AbstractClass
    def generate_report(self):
        self.collect_data()
        self.format_data()
        self.generate_header()
        self.generate_body()
        self.generate_footer()
        self.output_report()

    def collect_data(self):
        raise NotImplementedError("Subclasses must implement this method")

    def format_data(self):
        raise NotImplementedError("Subclasses must implement this method")

    def generate_header(self):
        print("Generating default header")

    def generate_footer(self):
        print("Generating default footer")

    def output_report(self):
        print("Outputting report to console")


class SalesReportGenerator(ReportGenerator):  # ConcreteClass
    def collect_data(self):
        print("Collecting sales data")
        self.sales_data = ["Sales 1", "Sales 2", "Sales 3"]

    def format_data(self):
        print("Formatting sales data")
        self.formatted_sales_data = "\n".join(self.sales_data)

    def generate_header(self):
        print("Generating Sales Report Header")

    def generate_body(self):
        print("Generating Sales Report Body")
        print(self.formatted_sales_data)


class PerformanceReportGenerator(ReportGenerator):  # ConcreteClass
    def collect_data(self):
        print("Collecting performance data")
        self.performance_data = ["Perf 1", "Perf 2", "Perf 3"]

    def format_data(self):
        print("Formatting performance data for web output")
        self.formatted_performance_data = "<br>".join(self.performance_data)

    def generate_body(self):
        print("Generating Performance Report Body")
        print(self.formatted_performance_data)

    def output_report(self):
        print("Outputting report to web page")


if __name__ == "__main__":
    sales_report = SalesReportGenerator()
    sales_report.generate_report()

    performance_report = PerformanceReportGenerator()
    performance_report.generate_report()
