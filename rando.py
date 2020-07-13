# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np

# Create a new web app.
app = fl.Flask(__name__)

# Add root route.
@app.route('/')
def stdnor():
  return {"value": np.random.standard_normal()}