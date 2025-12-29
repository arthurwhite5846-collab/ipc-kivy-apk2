from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class IPCApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # ======= INPUT FIELDS =======
        # input_filter='float' helps restrict input to numbers on both desktop and mobile
        self.total_theoretical = TextInput(hint_text="Total Theoretical (kg)", multiline=False, input_filter='float')
        self.lot1_assay = TextInput(hint_text="Lot 1 Assay %", multiline=False, input_filter='float')
        self.lot1_moisture = TextInput(hint_text="Lot 1 Moisture %", multiline=False, input_filter='float')
        self.lot1_weight = TextInput(hint_text="Lot 1 Actual Weight (kg)", multiline=False, input_filter='float')
        self.lot2_assay = TextInput(hint_text="Lot 2 Assay %", multiline=False, input_filter='float')
        self.lot2_moisture = TextInput(hint_text="Lot 2 Moisture %", multiline=False, input_filter='float')

        # ======= RESULT LABEL =======
        self.result_label = Label(text="Lot 2 Required Weight: -- kg", font_size=28)

        # ======= CALCULATE BUTTON =======
        calculate_btn = Button(text="CALCULATE", size_hint=(1, 0.8))
        calculate_btn.bind(on_press=self.calculate)

        # ======= ADD WIDGETS TO LAYOUT =======
        for widget in [
            self.total_theoretical,
            self.lot1_assay,
            self.lot1_moisture,
            self.lot1_weight,
            self.lot2_assay,
            self.lot2_moisture
        ]:
            layout.add_widget(widget)

        layout.add_widget(calculate_btn)
        layout.add_widget(self.result_label)

        # ======= FOOTER =======
        footer = Label(
            text="Made by: Dr Ahmed Nader",
            font_size=20,
            size_hint=(1, 0.1)
        )
        layout.add_widget(footer)

        return layout

    # ======= CALCULATION FUNCTION =======
    def calculate(self, instance):
        try:
            total_theoretical = float(self.total_theoretical.text)
            lot1_assay = float(self.lot1_assay.text)
            lot1_moisture = float(self.lot1_moisture.text)
            lot1_weight = float(self.lot1_weight.text)
            lot2_assay = float(self.lot2_assay.text)
            lot2_moisture = float(self.lot2_moisture.text)

            # Effective % for each lot
            lot1_effective = (lot1_assay * (100 - lot1_moisture)) / 100
            lot2_effective = (lot2_assay * (100 - lot2_moisture)) / 100

            if lot2_effective <= 0:
                self.result_label.text = "Lot 2 Effective % must be > 0"
                return

            # Theoretical covered by Lot 1
            theoretical_from_lot1 = lot1_weight * (lot1_effective / 100)

            # Remaining theoretical
            remaining_theoretical = total_theoretical - theoretical_from_lot1

            # Weight required from Lot 2
            lot2_required = remaining_theoretical / (lot2_effective / 100)

            self.result_label.text = f"Lot 2 Required Weight: {lot2_required:.6f} kg"

        except Exception:
            self.result_label.text = "Please enter valid numbers"


if __name__ == "__main__":
    IPCApp().run()
