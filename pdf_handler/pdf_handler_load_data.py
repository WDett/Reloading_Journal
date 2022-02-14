from fpdf import FPDF
import os
from datetime import datetime
import subprocess
import main as main


class PDF(FPDF):
    def lines(self):
        self.set_line_width(0.0)
        self.line(5.0, 5.0, 210.0, 5.0)  # top one
        self.line(5.0, 274.0, 210.0, 274.0)  # bottom one
        self.line(5.0, 5.0, 5.0, 274.0)  # left one
        self.line(210.0, 5.0, 210.0, 274.0)  # right one
        self.line(5.0, 14.0, 210.0, 14.0)  # line under title section
        self.line(5.0, 40.0, 210.0, 40.0)  # line under load section
        self.line(5.0, 72.0, 210.0, 72.0)  # line under brass section
        self.line(5.0, 92.0, 210.0, 92.0)  # line under primer section
        self.line(5.0, 112.0, 210.0, 112.0)  # line under powder section
        self.line(5.0, 132.0, 210.0, 132.0)  # line under projectile section
        self.line(5.0, 267.0, 210.0, 267.0)  # line under notes section

    def add_load_name(self, load_name):
        self.set_xy(0.0, 0.0)
        self.set_font('Arial', 'B', 16)
        self.set_text_color(0, 0, 0)
        self.cell(w=210.0, h=20.0, align='C', txt=load_name, border=0)

    def add_exported_line(self, exported_line):
        self.set_xy(0.0, 270.0)
        self.set_font('Arial', '', 9)
        self.set_text_color(0, 0, 0)
        self.cell(w=215.0, h=1, align='C', txt=exported_line, border=0)

    def add_headers(self, text_header, x, y):
        self.set_xy(x, y)
        self.set_font('Arial', 'B', 13)
        self.set_text_color(150, 150, 150)
        self.cell(w=100.0, h=20.0, align='L', txt=text_header, border=0)

    def add_field_name(self, text_header, x, y):
        self.set_xy(x, y)
        self.set_font('Arial', 'B', 10)
        self.set_text_color(0, 0, 0)
        self.cell(w=20.0, h=20.0, align='R', txt=text_header, border=0)

    def add_field_value(self, text_header, x, y):
        self.set_xy(x, y)
        self.set_font('Arial', '', 10)
        self.set_text_color(0, 0, 0)
        self.cell(w=100.0, h=20.0, align='L', txt=text_header, border=0)

    def add_cartridge_box(self, text_header, x, y):
        self.set_xy(x, y)
        self.set_font('Arial', 'B', 12)
        self.set_text_color(0, 0, 0)
        self.cell(w=100.0, h=20.0, align='L', txt=text_header, border=0)

    def add_text_box(self, text_header, x, y):
        self.set_xy(x, y)
        self.set_font('Arial', '', 9)
        self.set_text_color(0, 0, 0)
        self.cell(w=100.0, h=20.0, align='L', txt=text_header, border=0)

    def add_notes(self, text_header, x, y):
        self.set_xy(x, y)
        self.set_font('Arial', '', 10)
        self.set_text_color(0, 0, 0)
        self.multi_cell(w=195.0, h=5.0, align='L', txt=text_header, border=0)


def generate_load_pdf(load_data):
    column_a = 11
    column_b = 80
    column_c = 140
    date_time = datetime.now()
    output_directory = f'{os.getcwd()}\\output\\'
    output_filename = f'{load_data[1]} - {load_data[0]}-Load Sheet.pdf'
    pdf = PDF(orientation='P', unit='mm', format='Letter')
    pdf.set_auto_page_break('true', 0)
    pdf.add_page()
    pdf.lines()
    pdf.add_load_name(load_data[1])

    pdf.add_headers('LOAD', 5, 8)
    pdf.add_field_name('NAME:', column_a, 16)
    pdf.add_field_value(f'{load_data[1]}', column_a + 20, 16)
    pdf.add_field_name('ID #:', column_c, 16)
    pdf.add_field_value(f'{load_data[0]}', column_c + 20, 16)
    pdf.add_field_name('CARTRIDGE:', column_a, 22)
    pdf.add_field_value(f'{load_data[2]}', column_a + 20, 22)
    pdf.add_field_name('COAL:', column_b, 22)
    pdf.add_field_value(f'{load_data[3]}', column_b + 20, 22)
    pdf.add_field_name('VELOCITY:', column_c, 22)
    pdf.add_field_value(f'{load_data[4]}', column_c + 20, 22)

    pdf.add_headers('BRASS', 5, 34)
    pdf.add_field_name('BRAND:', column_a, 42)
    pdf.add_field_value(f'{load_data[5]}', column_a + 20, 42)
    pdf.add_field_name('FIRINGS:', column_b, 42)
    pdf.add_field_value(f'{load_data[6]}', column_b + 20, 42)
    pdf.add_field_name('LENGTH:', column_c, 42)
    pdf.add_field_value(f'{load_data[7]}', column_c + 20, 42)
    pdf.add_field_name('TUMBLED:', column_a, 48)
    pdf.add_field_value(f'{load_data[8]}', column_a + 20, 48)
    pdf.add_field_name('ANNEALED:', column_b, 48)
    pdf.add_field_value(f'{load_data[9]}', column_b + 20, 48)
    pdf.add_field_name('TRIMMED:', column_c, 48)
    pdf.add_field_value(f'{load_data[10]}', column_c + 20, 48)
    pdf.add_field_name('CHAMFER:', column_a, 54)
    pdf.add_field_value(f'{load_data[11]}', column_a + 20, 54)
    pdf.add_field_name('DEBURRED:', column_b, 54)
    pdf.add_field_value(f'{load_data[12]}', column_b + 20, 54)
    pdf.add_field_name('CRIMP:', column_c, 54)
    pdf.add_field_value(f'{load_data[13]} @ {load_data[14]}', column_c + 20, 54)

    pdf.add_headers('PRIMER', 5, 66)
    pdf.add_field_name('BRAND:', column_a, 74)
    pdf.add_field_value(f'{load_data[15]}', column_a + 20, 74)
    pdf.add_field_name('MODEL:', column_b, 74)
    pdf.add_field_value(f'{load_data[16]}', column_b + 20, 74)

    pdf.add_headers('POWDER', 5, 86)
    pdf.add_field_name('BRAND:', column_a, 94)
    pdf.add_field_value(f'{load_data[17]}', column_a + 20, 94)
    pdf.add_field_name('MODEL:', column_b, 94)
    pdf.add_field_value(f'{load_data[18]}', column_b + 20, 94)
    pdf.add_field_name('GRAINS:', column_c, 94)
    pdf.add_field_value(f'{load_data[19]}', column_c + 20, 94)

    pdf.add_headers('PROJECTILE', 5, 106)
    pdf.add_field_name('BRAND:', column_a, 114)
    pdf.add_field_value(f'{load_data[20]}', column_a + 20, 114)
    pdf.add_field_name('MODEL:', column_b, 114)
    pdf.add_field_value(f'{load_data[21]}', column_b + 20, 114)
    pdf.add_field_name('GRAINS:', column_c, 114)
    pdf.add_field_value(f'{load_data[22]}', column_c + 20, 114)
    pdf.add_headers('NOTES', 5, 126)
    pdf.add_notes(f'{load_data[23]}', 10, 140)

    pdf.add_exported_line(f'Report exported by Reloading Journal {main.version} on {date_time.strftime("%B %d, %Y")} '
                          f'at {date_time.strftime("%H:%M:%S")}')

    check_if_exists = os.path.exists(output_directory)
    if not check_if_exists:
        os.makedirs(output_directory)
    pdf.output(output_directory + output_filename, 'F')
    subprocess.Popen([output_directory + output_filename], shell=True)


def generate_box_pdf(load_data):
    date_time = datetime.now()
    output_directory = f'{os.getcwd()}\\output\\'
    output_filename = f'{load_data[1]} - {load_data[0]}-Box Labels.pdf'
    pdf = PDF(orientation='P', unit='mm', format='Letter')
    pdf.set_auto_page_break('true', 0)
    pdf.add_page()
    number_of_rows = 5
    row_height = 0
    current_row = 1
    while current_row <= number_of_rows:
        column_a = 5
        column_b = 110
        number_of_columns = 2
        current_column = 1
        column_location = column_a
        while current_column <= number_of_columns:
            pdf.add_cartridge_box(f'{load_data[2]}          {date_time.strftime("%m/%d/%Y")}', column_location,
                                  row_height)
            pdf.add_text_box(f'{load_data[1]}', column_location, row_height + 5)
            pdf.add_text_box(f'COAL:  '
                             f'{load_data[3]}         \tVELOCITY:  {load_data[4]}', column_location, row_height + 9)
            pdf.add_text_box(f'BRASS:  '
                             f'{load_data[5]}        \tFIRINGS: {load_data[6]}', column_location, row_height + 13)
            pdf.add_text_box(f'CRIMP:  '
                             f'{load_data[13]} @ {load_data[14]}', column_location, row_height + 17)
            pdf.add_text_box(f'PRIMER:  '
                             f'{load_data[15]} {load_data[16]}', column_location, row_height + 21)
            pdf.add_text_box(f'POWDER:  '
                             f'{load_data[17]} {load_data[18]} @ {load_data[19]}GN', column_location, row_height + 25)
            pdf.add_text_box(f'PROJECTILE:  '
                             f'{load_data[20]} {load_data[21]} {load_data[22]}GN', column_location, row_height + 29)
            pdf.add_text_box(f'ID:  '
                             f'{load_data[0]}   '
                             f'LOT:  '
                             f'{date_time.strftime("%Y%m%d%H%M%S")}GN', column_location, row_height + 33)
            current_column = current_column + 1
            column_location = column_b
        current_row = current_row + 1
        row_height = row_height + 50
    check_if_exists = os.path.exists(output_directory)
    if not check_if_exists:
        os.makedirs(output_directory)
    pdf.output(output_directory + output_filename, 'F')
    subprocess.Popen([output_directory + output_filename], shell=True)
