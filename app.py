import tkinter as tk
from tkinter import font as tkfont
from helpers import get_max_edge, get_area, convert_to_seconds, set_lable_concat, clear_entries
import random


class AssessmentApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.resizable(False, False)
        self.geometry('425x300')
        self.title('PPA')
        self.title_font = tkfont.Font(
            family='Helvetica', size=18, weight='bold')

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for f in (Menu, Area, MaxEdge, ConvertHoursMinutes, Recursion, Help):
            page_name = f.__name__
            frame = f(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame('Menu')

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Python Programming Assessment',
                         font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)

        btn_area = tk.Button(self, text='Calculate Area',
                             command=lambda: controller.show_frame('Area'),
                             height=2,
                             width=20)
        btn_edge = tk.Button(self, text='Calculate Mex Edge',
                             command=lambda: controller.show_frame('MaxEdge'),
                             height=2,
                             width=20)
        btn_hr_min = tk.Button(self, text='Convert Hrs/Mins',
                               command=lambda: controller.show_frame(
                                   'ConvertHoursMinutes'),
                               height=2,
                               width=20)
        btn_recursion = tk.Button(self, text='Recursion',
                                  command=lambda: controller.show_frame(
                                      'Recursion'),
                                  height=2,
                                  width=20)
        btn_tut = tk.Button(self, text='Help',
                            command=lambda: controller.show_frame('Help'),
                            height=2,
                            width=20)
        btn_area.pack()
        btn_edge.pack()
        btn_hr_min.pack()
        btn_recursion.pack()
        btn_tut.pack()


class Area(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Area of a triangle',
                         font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)

        frm_fields = tk.Frame(self)

        lbl_side_a = tk.Label(frm_fields, text='A')
        lbl_side_b = tk.Label(frm_fields, text='B')
        lbl_side_c = tk.Label(frm_fields, text='C')
        lbl_area = tk.Label(frm_fields, text='Area')

        ent_side_a = tk.Entry(frm_fields)
        ent_side_b = tk.Entry(frm_fields)
        ent_side_c = tk.Entry(frm_fields)
        ent_area = tk.Entry(frm_fields)

        lbl_side_a.grid(row=0, column=1)
        ent_side_a.grid(row=0, column=2)

        lbl_side_b.grid(row=1, column=1)
        ent_side_b.grid(row=1, column=2)

        lbl_side_c.grid(row=2, column=1, pady=(0, 20))
        ent_side_c.grid(row=2, column=2, pady=(0, 20))

        lbl_area.grid(row=3, column=1, pady=(0, 20))
        ent_area.grid(row=3, column=2, pady=(0, 20))

        frm_fields.pack()

        frm_buttons = tk.Frame(self)

        btn_area = tk.Button(frm_buttons, text='Get Area',
                             command=lambda: get_area(
                                 ent_area,
                                 ent_side_a.get(),
                                 ent_side_b.get(),
                                 ent_side_c.get()
                             ),
                             height=2,
                             width=10,
                             fg='white',
                             bg='#28a745')

        btn_clear = tk.Button(frm_buttons, text='Clear',
                              command=lambda: clear_entries(
                                  [ent_side_a, ent_side_b, ent_side_c, ent_area]
                              ),
                              height=2,
                              width=10,
                              fg='white',
                              bg='#ffc107')

        button = tk.Button(frm_buttons, text='Menu',
                           command=lambda: controller.show_frame('Menu'),
                           height=2,
                           width=10,
                           fg='white',
                           bg='#17a2b8')

        btn_area.grid(row=0, column=1)
        btn_clear.grid(row=0, column=2)
        button.grid(row=0, column=3)

        frm_buttons.pack()


class MaxEdge(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Max edge of a triangle',
                         font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)

        frm_fields = tk.Frame(self)

        lbl_side_a = tk.Label(frm_fields, text='A')
        lbl_side_b = tk.Label(frm_fields, text='B')
        lbl_max = tk.Label(frm_fields, text='Max Edge')

        ent_side_a = tk.Entry(frm_fields)
        ent_side_b = tk.Entry(frm_fields)
        ent_max = tk.Entry(frm_fields)

        lbl_side_a.grid(row=0, column=1)
        ent_side_a.grid(row=0, column=2)

        lbl_side_b.grid(row=1, column=1, pady=(0, 20))
        ent_side_b.grid(row=1, column=2, pady=(0, 20))

        lbl_max.grid(row=3, column=1, pady=(0, 20))
        ent_max.grid(row=3, column=2, pady=(0, 20))

        frm_fields.pack()

        frm_buttons = tk.Frame(self)

        btn_max = tk.Button(frm_buttons, text='Get Max',
                            command=lambda: get_max_edge(
                                ent_max,
                                ent_side_a.get(),
                                ent_side_b.get(),
                            ),
                            height=2,
                            width=10,
                            fg='white',
                            bg='#28a745')

        btn_clear = tk.Button(frm_buttons, text='Clear',
                              command=lambda: clear_entries(
                                  [ent_side_a, ent_side_b, ent_max]
                              ),
                              height=2,
                              width=10,
                              fg='white',
                              bg='#ffc107')

        button = tk.Button(frm_buttons, text='Menu',
                           command=lambda: controller.show_frame('Menu'),
                           height=2,
                           width=10,
                           fg='white',
                           bg='#17a2b8')

        btn_max.grid(row=0, column=1)
        btn_clear.grid(row=0, column=2)
        button.grid(row=0, column=3)

        frm_buttons.pack()


class ConvertHoursMinutes(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Hrs/Mins to Seconds',
                         font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)

        frm_fields = tk.Frame(self)

        lbl_hrs = tk.Label(frm_fields, text='Hours')
        lbl_mins = tk.Label(frm_fields, text='Minutes')
        lbl_conversion = tk.Label(frm_fields, text='Seconds')

        ent_hrs = tk.Entry(frm_fields)
        ent_mins = tk.Entry(frm_fields)
        ent_seconds = tk.Entry(frm_fields)

        lbl_hrs.grid(row=0, column=1)
        ent_hrs.grid(row=0, column=2)

        lbl_mins.grid(row=1, column=1, pady=(0, 20))
        ent_mins.grid(row=1, column=2, pady=(0, 20))

        lbl_conversion.grid(row=3, column=1, pady=(0, 20))
        ent_seconds.grid(row=3, column=2, pady=(0, 20))

        frm_fields.pack()

        frm_buttons = tk.Frame(self)

        btn_convert = tk.Button(frm_buttons, text='Convert',
                                command=lambda: convert_to_seconds(
                                    ent_seconds,
                                    ent_hrs.get(),
                                    ent_mins.get(),
                                ),
                                height=2,
                                width=10,
                                fg='white',
                                bg='#28a745')

        btn_clear = tk.Button(frm_buttons, text='Clear',
                              command=lambda: clear_entries(
                                  [ent_hrs, ent_mins, ent_seconds]
                              ),
                              height=2,
                              width=10,
                              fg='white',
                              bg='#ffc107')

        button = tk.Button(frm_buttons, text='Menu',
                           command=lambda: controller.show_frame('Menu'),
                           height=2,
                           width=10,
                           fg='white',
                           bg='#17a2b8')

        btn_convert.grid(row=0, column=1)
        btn_clear.grid(row=0, column=2)
        button.grid(row=0, column=3)

        frm_buttons.pack()


class Recursion(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='So you want to repeat stuff?',
                         font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)

        frm_fields = tk.Frame(self)

        lbl_text = tk.Label(frm_fields, text='Text')
        lbl_time = tk.Label(frm_fields, text='Times')
        lbl_repeated = tk.Label(frm_fields, height=2)

        ent_text = tk.Entry(frm_fields)
        ent_times = tk.Entry(frm_fields)
        ent_repeated = tk.Entry(frm_fields)

        lbl_text.grid(row=0, column=1)
        ent_text.grid(row=0, column=2)

        lbl_time.grid(row=1, column=1, pady=(0, 20))
        ent_times.grid(row=1, column=2, pady=(0, 20))

        lbl_repeated.grid(row=3, column=2, pady=(0, 20))
        ent_repeated.grid(row=3, column=2, pady=(0, 20))

        frm_fields.pack()

        frm_buttons = tk.Frame(self)

        btn_recur = tk.Button(frm_buttons, text='Recur',
                              command=lambda: set_lable_concat(
                                  ent_repeated,
                                  ent_times.get(),
                                  ent_text.get(),
                              ),
                              height=2,
                              width=10,
                              fg='white',
                              bg='#28a745')

        btn_clear = tk.Button(frm_buttons, text='Clear',
                              command=lambda: clear_entries(
                                  [ent_times, ent_text, ent_repeated]
                              ),
                              height=2,
                              width=10,
                              fg='white',
                              bg='#ffc107')

        button = tk.Button(frm_buttons, text='Menu',
                           command=lambda: controller.show_frame('Menu'),
                           height=2,
                           width=10,
                           fg='white',
                           bg='#17a2b8')

        btn_recur.grid(row=0, column=1)
        btn_clear.grid(row=0, column=2)
        button.grid(row=0, column=3)

        frm_buttons.pack()


class Help(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Help',
                         font=controller.title_font)
        label.pack(side='top', fill='x', pady=2)

        frm_text = tk.Frame(self, pady=2)
        scr_scroll = tk.Scrollbar(frm_text)
        txt = tk.Text(frm_text, wrap="word",
                      yscrollcommand=scr_scroll.set, height=12, width=60)
        txt.tag_configure('section', font=('Helvetica', 12, 'bold'))
        txt.tag_configure('paragraph', font=('Helvetica', 10))
        txt.insert(1.0, 'Calculate Area:\n', 'section')
        txt.insert(
            'end',
            'Given the length of the 3 edges of a triangle this will return the given area. Insert the value of the edges and click \'Get Area\'.\n',
            'paragraph'
        )
        txt.insert('end', '\nCalculate Max Edge:\n', 'section')
        txt.insert(
            'end',
            'Given the length of the 2 sides of a triangle this will return the maximun length of the final edge. Insert the value of the two edges and click \'Get Max\'.\n',
            'paragraph'
        )
        txt.insert('end', '\nConvert Hrs/Mins:\n', 'section')
        txt.insert(
            'end',
            'Given numeric values for hours or minutes this will return the conversion to seconds. Insert either value and click \'Convert\'.\n',
            'paragraph'
        )
        txt.insert('end', '\nRecursion:\n', 'section')
        txt.insert(
            'end',
            'Given a string and number this will return the value repeated the specified number of times using a recursive function. Insert a string and a number and click \'Recur\'.\n',
            'paragraph'
        )
        txt.configure(state='disabled')

        scr_scroll.pack(side='right', fill='y')
        txt.pack(side='left')
        frm_text.pack()

        button = tk.Button(self, text='Menu',
                           command=lambda: controller.show_frame('Menu'),
                           height=2,
                           width=10,
                           fg='white',
                           bg='#17a2b8')
        button.pack()


if __name__ == '__main__':
    app = AssessmentApp()
    app.mainloop()
