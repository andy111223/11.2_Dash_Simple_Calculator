import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

# Create the app
app = dash.Dash()

# Create the layout
app.layout = html.Div(
    style={
        'background-color': '#121212',  
        'color': '#ffffff',  
        'height': '100vh',  
        'display': 'flex',  
        'justify-content': 'center', 
        'align-items': 'center',  
    },
    children=[
        html.Div(
            style={
                'background-color': '#222222', 
                'padding': '20px',
                'border-radius': '10px',
                'box-shadow': '0px 4px 10px rgba(0, 0, 0, 0.5)',
                'width': '400px',  
                'text-align': 'center'
            },
            children=[
                html.H1(
                    'Simple Dash Calculator',
                    style={
                        'color': '#FF00FF',  
                        'font-size': '30px',
                        'margin-bottom': '20px'
                    }
                ),
                html.Label(
                    'Factor #1: ',
                    style={
                        'font-size': '20px',
                        'color': '#00FFFF'  
                    }
                ),
                dcc.Input(
                    id='product-1',
                    placeholder='Enter a number',
                    type='number',
                    value='',
                    style={
                        'width': 'calc(100% - 20px)',  
                        'font-size': '20px',
                        'padding': '10px',
                        'margin-bottom': '10px',
                        'border': '2px solid #FF4500',  
                        'border-radius': '5px',
                        'background-color': '#333333',
                        'color': '#ffffff',
                        'box-sizing': 'border-box'  
                    }
                ),
                html.Label(
                    'Factor #2: ',
                    style={
                        'font-size': '20px',
                        'color': '#00FF00'  
                    }
                ),
                dcc.Input(
                    id='product-2',
                    placeholder='Enter a number',
                    type='number',
                    value='',
                    style={
                        'width': 'calc(100% - 20px)',  
                        'font-size': '20px',
                        'padding': '10px',
                        'margin-bottom': '20px',
                        'border': '2px solid #1E90FF',  
                        'border-radius': '5px',
                        'background-color': '#333333',
                        'color': '#ffffff',
                        'box-sizing': 'border-box'  
                    }
                ),
                html.Div(
                    children=[
                        html.Button(
                            'Add',
                            id='add-btn',
                            style={
                                'font-size': '20px',
                                'margin': '5px',
                                'padding': '10px 20px',
                                'background-color': '#FF6347',  
                                'border': 'none',
                                'color': '#ffffff',
                                'border-radius': '5px',
                                'cursor': 'pointer'
                            }
                        ),
                        html.Button(
                            'Sub',
                            id='sub-btn',
                            style={
                                'font-size': '20px',
                                'margin': '5px',
                                'padding': '10px 20px',
                                'background-color': '#32CD32',  
                                'border': 'none',
                                'color': '#ffffff',
                                'border-radius': '5px',
                                'cursor': 'pointer'
                            }
                        ),
                        html.Button(
                            'Mul',
                            id='mul-btn',
                            style={
                                'font-size': '20px',
                                'margin': '5px',
                                'padding': '10px 20px',
                                'background-color': '#1E90FF',  
                                'border': 'none',
                                'color': '#ffffff',
                                'border-radius': '5px',
                                'cursor': 'pointer'
                            }
                        ),
                        html.Button(
                            'Div',
                            id='div-btn',
                            style={
                                'font-size': '20px',
                                'margin': '5px',
                                'padding': '10px 20px',
                                'background-color': '#8A2BE2',  
                                'border': 'none',
                                'color': '#ffffff',
                                'border-radius': '5px',
                                'cursor': 'pointer'
                            }
                        ),
                    ]
                ),
                html.Div(
                    id='output',
                    style={
                        'font-size': '30px',
                        'margin-top': '20px',
                        'color': '#FFD700'  
                    }
                )
            ]
        )
    ]
)
# Create callbacks
@app.callback(
    Output('output','children'),
    [Input('add-btn','n_clicks'),Input('sub-btn','n_clicks'),Input('mul-btn','n_clicks'),Input('div-btn','n_clicks')],
    [State('product-1', 'value'),State('product-2', 'value')]
)
def calculate(add_clicks, sub_clicks, mul_clicks, div_clicks, prod_1, prod_2):
    
    ctx = dash.callback_context # Determines which Input triggered the callback
    if not ctx.triggered:
        return "Enter numbers and click a button"
    
    if prod_1 is None or prod_2 is None:
        return "Enter valid numbers"
    
    prod_1 = float(prod_1)
    prod_2 = float(prod_2)

    # button_id = ctx.triggered[0]['prop_id'].split('.')[0]  # Get the ID of the triggered button
    button_id = ctx.triggered_id 

    if button_id == 'add-btn':
        return prod_1 + prod_2
    elif button_id == 'sub-btn':
        return prod_1 - prod_2
    elif button_id == 'mul-btn':
        return prod_1 * prod_2
    elif button_id == 'div-btn':
        if prod_2 != 0:
            return prod_1 / prod_2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"


# Run the server
if __name__ == '__main__':
    app.run_server()