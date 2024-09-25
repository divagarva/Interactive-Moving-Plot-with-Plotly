import numpy as np
import plotly.graph_objects as go

# Generate data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a scatter plot
fig = go.Figure()

# Add the trace with initial data
fig.add_trace(go.Scatter(x=[x[0]], y=[y[0]], mode="markers", marker=dict(size=10, color="red")))

# Update the plot frames for the animation
frames = [go.Frame(data=[go.Scatter(x=[x[i]], y=[y[i]])]) for i in range(len(x))]

# Add frames to the figure
fig.frames = frames

# Define the layout with the animation configuration
fig.update_layout(
    updatemenus=[
        {
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 50, "redraw": True}, "fromcurrent": True}],
                    "label": "Play",
                    "method": "animate",
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate"}],
                    "label": "Pause",
                    "method": "animate",
                },
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top",
        }
    ]
)

# Show the plot
fig.show()
