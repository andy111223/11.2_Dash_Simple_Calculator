# Simple Dash Calculator

**Have you ever wanted a straightforward way to perform basic calculations with only two numbers?** This simple calculator handles exactly that: addition, subtraction, multiplication, and division for two numbers, presented in an interactive and user-friendly web app.

This app demonstrates the author's proficiency in using Dash's powerful components such as `dcc`, `dash.html`, and callback mechanisms (`Input`, `Output`, `State`) to create a responsive and educational tool.

---

### Features:
- **Four operations:** Add, Subtract, Multiply, Divide
- **Two number inputs:** Handles calculations for only two numbers
- **Responsive design:** Works on any modern web browser
- **Educational purpose:** Showcases interactivity through Dash's callback mechanisms

---

### Usage Instructions:
1. Open your terminal.
2. Run the app:
   ```bash
   python app.py
   ```
3. The app opens at [http://127.0.0.1:8050/](http://127.0.0.1:8050/).
   - If necessary, change the port by modifying `app.run_server()`:
     ```python
     app.run_server(port=8051)
     ```

---

### App Layout:
1. **Input Fields**: Enter two numbers (Factor #1 and Factor #2).
2. **Operation Buttons**: 
   - **Add**: Adds the two numbers.
   - **Subtract**: Subtracts the second number from the first.
   - **Multiply**: Multiplies the two numbers.
   - **Divide**: Divides the first number by the second (division by zero is handled gracefully).
3. **Result Display**: Shows the result of the operation.

---

### Libraries and Components Used:
- **Dash**: The core framework for building this app.
  - `dcc.Input`: For numeric inputs.
  - `dcc.Button`: For operation buttons.
- **Dash HTML Components (`dash.html`)**: Used for structuring the layout with `Div`, `Label`, and other HTML-like components.
- **Dash Callbacks**:
  - `Input`: Tracks which button was clicked.
  - `State`: Retrieves values from input fields.
  - `Output`: Displays the result in the designated output section.
  - `dash.callback_context`: Dynamically determines which button triggered the callback.
- **Python Standard Libraries**:
  - String and number manipulations to handle calculations and display messages.

---

### Author's Notes:
- This app demonstrates the author's **proficiency in Dash components and callback mechanisms**.
- Designed for **educational purposes only**, showcasing an interactive implementation of basic mathematical operations.

---

### Repository:
The code for this app is hosted at:  
[https://github.com/andy111223/11.2_Dash_Simple_Calculator.git](https://github.com/andy111223/11.2_Dash_Simple_Calculator.git)

---

### Dependencies:
- **Python**: 3.12.3
- **Dash**: 2.18.2

---

**Enjoy your calculations and feel free to explore the app for further learning!** 🎉