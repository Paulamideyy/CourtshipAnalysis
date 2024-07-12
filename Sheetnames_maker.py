from openpyxl import Workbook
import os

def create_excel_with_sheets(sheet_names, file_path):
    # Create a new Workbook object
    wb = Workbook()

    # Loop through the sheet names and create sheets accordingly
    for index, name in enumerate(sheet_names, start=1):
        # Truncate the sheet name if it exceeds 31 characters
        if len(name) > 31:
            name = name[:31]
        # Create a new sheet
        ws = wb.create_sheet(title=name, index=index)

        # Add common header
        header = ['manual t0', 'manual t1', 'JAABA t0', 'JAABA t1', 'Matebook t0', 'Matebook t1']  # Add your desired headers here
        ws.append(header)

    # Remove the default sheet created by openpyxl (Sheet)
    wb.remove(wb["Sheet"])

    # Save the workbook
    wb.save(file_path)
    print(f"Excel file '{file_path}' with specified sheets and common header created successfully.")

def main():
    # Input sheet names
    sheet_names = ['testDVGH_1', 'testDVGH_2', 'testDVGH_3', 'testDVGH_5', 'testDVGH_4', 'testDVGH_6', 'testDVGH_7', 'testDVGH_8', 'testDVGH_9']

    # Directory path to save the Excel file 
    directory_path = "E:\Paulami\Ground-truthing Data\Attempted copulation classifier\DecapVirgins\AC_13"

    # File name for the Excel file
    file_name = "Attempted_cop_decap_workbook.xlsx"

    # Combine directory path and file name
    file_path = os.path.join(directory_path, file_name)

    # Create Excel file with specified sheet names and common header
    create_excel_with_sheets(sheet_names, file_path)

if __name__ == "__main__":
    main()


