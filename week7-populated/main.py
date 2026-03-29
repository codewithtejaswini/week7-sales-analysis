#!/usr/bin/env python3

\"\"\"Main CLI entry point for sales analysis dashboard.\"\"\"
import argparse
import logging
import sys
from pathlib import Path
from sales_analyzer import SalesAnalyzer, create_visualizations, generate_excel_report, print_console_summary

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description='Sales Data Analysis Dashboard')
    parser.add_argument('data_path', help='Path to sales data CSV file')
    parser.add_argument('--clean', action='store_true', help='Clean data only')
    parser.add_argument('--analyze', action='store_true', help='Run analysis and print summary')
    parser.add_argument('--visualize', action='store_true', help='Create visualizations')
    parser.add_argument('--report', action='store_true', help='Generate Excel report')
    parser.add_argument('--output-dir', default='output', help='Output directory for viz/reports')
    
    args = parser.parse_args()
    
    if not Path(args.data_path).exists():
        print(f"❌ Data file not found: {args.data_path}")
        sys.exit(1)
    
    print("🚀 Starting Sales Analysis Dashboard")
    print(f"📁 Data: {args.data_path}")
    
    # Initialize analyzer
    analyzer = SalesAnalyzer(args.data_path)
    
    if analyzer.df is None or analyzer.df.empty:
        print("❌ No valid data loaded. Exiting.")
        sys.exit(1)
    
    actions = []
    if args.clean:
        actions.append("clean")
    if args.analyze:
        actions.append("analyze")
    if args.visualize:
        actions.append("visualize")
    if args.report:
        actions.append("report")
    
    if not actions:
        # Default: full analysis
        args.analyze = args.visualize = args.report = True
        actions = ["analyze", "visualize", "report"]
    
    print(f"📋 Running: {', '.join(actions)}")
    
    # Run selected actions
    if 'clean' in actions:
        analyzer.clean_data()
    
    if 'analyze' in actions:
        print("\n" + "="*60)
        print_console_summary(analyzer)
        print("="*60)
    
    if 'visualize' in actions:
        print(f"\n📊 Creating visualizations in {args.output_dir}...")
        create_visualizations(analyzer.df, args.output_dir)
    
    if 'report' in actions:
        print("\n📄 Generating Excel report...")
        success = generate_excel_report(analyzer, f"{args.output_dir}/sales_report.xlsx")
        if not success:
            logger.error("Failed to generate report")
    
    print("\n✅ Analysis complete!")

if __name__ == "__main__":
    main()

