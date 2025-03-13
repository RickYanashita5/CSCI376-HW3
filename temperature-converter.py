from nicegui import ui

ui.colors(
      primary='#a629ff',
      secondary='#4fc8f0',
      accent='#f429ff',
      positive='#21BA45',
      negative='#ed001c',
      info='#3293ed',
      warning='#fff82e'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: the color of the text is the color #21BA45, defined as 'positive' in the set of theme colors
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4")
        # text-negative: the color of the text is the color #ed001c, defined as 'negative' in the set of theme colors

def convert_2():
    try: 
        temp = float(input_field_2.value)
        if conversion_type_2.value == "Celsius to Fahrenheit":
            result_label_2.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label_2.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label_2.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: the color of the text is the color #21BA45, defined as 'positive' in the set of theme colors
    except ValueError:
        result_label_2.set_text("Please enter a valid number.")
        result_label_2.classes("text-lg font-semibold text-negative mt-4")
        # text-negative: the color of the text is the color #ed001c, defined as 'negative' in the set of theme colors


with ui.row().classes("mx-auto"):
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl"):
        # w-100: Set element width to be fixed at 100
        # p-6: Set padding around content inside the card (all sides) to be fized at 6, which is 1.5rem or 24px
        # shadow-xl: Set the card to have a fixed shadow of size 'xl' & color light grey, which means a box-shadow of 0 25px 50px -12px. 
        # mx-auto: Set horizontal margin of the card, horizontally centers the card on the page
        # mt-10: Sets top margin of the card to be fixed at 10, which is 2.5rem or 40px
        # rounded-xl: Sets the border radius of the card to be fixed at size 'xl', which is a border radius of 0.75rem or 12px
        ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4 uppercase drop-shadow-sm tracking-wide text-center italic")
        # text-2xl: Set label text size to be fixed at size '2xl', which is 1.5rem or 24px
        # font-bold: Set label font size to be bold, which is font-weight 700; 
        # text-accent: Set label font color to #f429ff, defined as 'accent'
        # mb-4: Sets bottom margin of the label to be fized at 4, which is 1rem or 16px
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded")
        # w-full: Set field width to the full width of parent
        # border: Set field border to 1px solid border in grey color
        # rounded: Set border radius of field to be fixed at 0.25rem or 4px
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded")
        # text-white: Set button text font color to be white, #ffffff
        # py-2: Set button vertical padding to be fixed at 2, which is 0.5rem or 8px
        # px-4: Set button horizontal padding to be fixed at 4, which 1rem or 16px
        result_label = ui.label("").classes("text-lg mt-4")
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl"):
        ui.label("Temp Converter v2").classes("text-xl text-accent mb-4 drop-shadow-sm tracking-wide text-center")
        input_field_2 = ui.select([-30,-20,-10,0,10,20,30]).classes("w-full")
        conversion_type_2 = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        convert_button = ui.button("Convert", on_click=convert_2).classes("text-white font-bold py-2 px-4 rounded")
        result_label_2 = ui.label("").classes("text-lg mt-4")
ui.run()
