#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
from keras.models import load_model


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        NPTA = request.form.get('NPTA')
        TLTA = request.form.get('TLTA')
        WCTA = request.form.get('WCTA')
        model = load_model('BKRNN')
        pred = model.predict([[float(NPTA), float(TLTA), float(WCTA)]])
        print(pred)
        s = 'The predicted bankruptcy score is: ' + str(pred)
        return(render_template("index.html", result = s))
    else:
        return(render_template('index.html', result = ''))


# In[4]:


if __name__ == '__main__':
    app.run()


# In[ ]:



