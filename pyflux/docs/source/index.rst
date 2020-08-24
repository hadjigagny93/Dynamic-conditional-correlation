Introduction
==================================

What is PyFlux?
----------

PyFlux is a library for time series analysis and prediction. Users can choose from a flexible range of modelling and inference options, and use the output for forecasting and retrospection. Users can build a full probabilistic model where the data :math:`y` and latent variables (parameters) :math:`z` are treated as random variables through a joint probability :math:`p\left(y,z\right)`. The advantage of a probabilistic approach is that it gives a more complete picture of uncertainty, which is important for time series tasks such as forecasting. Alternatively, for speed, users can simply use Maximum Likelihood estimation for speed within the same unified API.

Installation
----------

The latest release version of PyFlux is available on PyPi. Python 2.7 and Python 3.5 are supported, but development occurs primarily on 3.5. To install ``pyflux``, simply call ``pip``: ::

  pip install pyflux

PyFlux requires a number of dependencies, in particular ``numpy``, ``pandas``, ``scipy``, ``patsy``, ``matplotlib``, ``numdifftools`` and ``seaborn``.

The development code can be accessed on `GitHub <http://www.github.com/RJT1990/pyflux>`_. The project is open source, and contributions are welcome and encouraged. We also encourage you to check out other modelling libraries written in Python including ``pymc3``, ``edward`` and ``statsmodels``.

Application Interface
----------

The PyFlux API is designed to be as clear and concise as possible, meaning it takes a minimal number of steps to conduct the model building process. The high-level outline is detailed below.

The first step is to **create a model instance**, where the main arguments are (i) a data input, such as a pandas dataframe, (ii) design parameters, such as autoregressive lags for an ARIMA model, and (iii) a family, which specifies the distribution of the modelled time series, such as a Normal distribution.

.. image:: http://www.pyflux.com/welcome_pack/introduction/model_api_1.png
  :align: center

::

  my_model = pf.ARIMA(data=my_dataframe, ar=2, ma=0, family=pf.Normal())

The second step is **prior formation**, which involves specifying a family for each latent variable in the model using the ``adjust_prior`` method, for example we can a prior for the constant in the ARIMA model :math:`N\left(0,10\right)`. The latent variables can be viewed by printing the ``latent_variables`` object attached to the model. Prior formation be ignored if the user is intending to just do Maximum Likelihood.

.. image:: http://www.pyflux.com/welcome_pack/introduction/model_api_2.png
  :align: center

::

  print(my_model.latent_variables)

  Index    Latent Variable     Prior           Prior Hyperparameters     V.I. Dist  Transform 
  ======== =================== =============== ========================= ========== ==========
  0        Constant            Normal          mu0: 0, sigma0: 3         Normal     None      
  1        AR(1)               Normal          mu0: 0, sigma0: 0.5       Normal     None      
  2        AR(2)               Normal          mu0: 0, sigma0: 0.5       Normal     None      
  3        Normal Scale        Flat            n/a (noninformative)      Normal     exp       
  
  my_model.adjust_prior(0, pf.Normal(0, 10))
  
  print(my_model.latent_variables)
  
  Index    Latent Variable     Prior           Prior Hyperparameters     V.I. Dist  Transform 
  ======== =================== =============== ========================= ========== ==========
  0        Constant            Normal          mu0: 0, sigma0: 10        Normal     None      
  1        AR(1)               Normal          mu0: 0, sigma0: 0.5       Normal     None      
  2        AR(2)               Normal          mu0: 0, sigma0: 0.5       Normal     None      
  3        Normal Scale        Flat            n/a (noninformative)      Normal     exp    

The third step is **model fitting (or inference)**, which involves using a ``fit`` method, specifying an inference option. Current options include Maximum Likelihood (MLE), Metropolis-Hastings (M-H), and black box variational inference (BBVI). Once complete, the model latent variable information will be updated, and the user can proceed to the post fitting methods.

.. image:: http://www.pyflux.com/welcome_pack/introduction/model_api_3.png
  :align: center

::

  x = my_model.fit('M-H')
  Tuning complete! Now sampling.
  Acceptance rate of Metropolis-Hastings is 0.2915
  
  x.summary()
  Normal ARIMA(2,0,0)                                                                                       
  ======================================== ==================================================
  Dependent Variable: sunspot.year         Method: Metropolis Hastings                       
  Start Date: 1702                         Unnormalized Log Posterior: -1219.7028            
  End Date: 1988                           AIC: 2447.40563132                                
  Number of observations: 287              BIC: 2462.04356018                                
  ===========================================================================================
  Latent Variable           Median             Mean               95% Credibility Interval 
  ========================= ================== ================== =========================
  Constant                  14.6129            14.5537            (11.8099 | 17.1807)       
  AR(1)                     1.3790             1.3796             (1.3105 | 1.4517)         
  AR(2)                     -0.6762            -0.6774            (-0.7484 | -0.6072)      
  Normal Scale              16.6720            16.6551            (15.5171 | 17.8696)      
  ===========================================================================================

::

  my_model.plot_z(figsize=(15, 7))

.. image:: http://www.pyflux.com/welcome_pack/introduction/output_6_1.png
  :align: center


The fourth step is **model evaluation**, **retrospection** and **prediction**. Once the model has been fit, the user can look at historical fit, criticize with posterior predictive checks, predict out of sample, and perform a range of other tasks for their model.

.. image:: http://www.pyflux.com/welcome_pack/introduction/model_api_4.png
  :align: center

::

  # Some example tasks
  my_model.plot_fit() # plots the fit of the model
  my_model.plot_sample(nsims=10) # draws samples from the model
  my_model.plot_ppc(T=np.mean) # plots histogram of posterior predictive check for mean
  my_model.plot_predict(h=5) # plots predictions for next 5 time steps
  my_model.plot_predict_is(h=5) # plots rolling in-sample prediction for past 5 time steps

  predictions = my_model.predict(h=5, intervals=True) # outputs dataframe of predictions
  samples = my_model.sample(nsims=10) # returns 10 samples from the data
  ppc_pvalue = my_model.ppc(T=np.mean) # p-value for mean posterior predictive test

Tutorials
----------

Want to learn how to use this library? Check out these tutorials:

.. toctree::
   :maxdepth: 2

   getting_started
   probabilistic_thinking
   inference
   evaluation_and_prediction

Model Guide
----------

.. toctree::
   :maxdepth: 2

   arima
   arimax
   dar
   dyn_lin
   egarch
   egarchm
   egarchmreg
   lmegarch
   segarch
   segarchm
   garch
   gas
   gas_llm
   gas_llt
   gas_rank
   gas_reg
   gasx
   gpnar
   llm
   llt
   dyn_glm
   nllm
   nllt
   var

Inference Guide
----------

.. toctree::
   :maxdepth: 2

   bayes
   classical
   families

Acknowledgements by the Author
----------

I am grateful to my employer `ALPIMA <http://www.alpima.net/>`_ for being supportive of my efforts to develop this library in my spare time. I am also grateful to those in the `PyData <http://www.pydata.org/>`_ community who have given helpful comments and feedback for development.

Ross Taylor, @rosstaylor90