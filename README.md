# ornstein_uhlenbeck
A Repository for Working with and Modelling a Simple Type of Stochastic Process

Ornstein Uhlenbeck Processes are in some sense the simplest nontrivial stochastic process satisfying 3 basic properties:

1. Stationarity- constant distribution over time (also shown below)
3. Gaussian Process:

Like the Weiner Process, the Ohrenstein Uhlenbeck Process can be viewed as a gaussian process. To see this, we begin with the Weiner Process as it is defined:

![eq1](https://latex.codecogs.com/svg.image?&space;dX_t=-\gamma(\mu-X_t)dt&plus;\sigma&space;W_t\quad(1))

And for the sake of simplicity we assume a mean (μ) of 0, which, along with two other conditions we impose on the process, will ensure that it is stationary.

We know that by Itô's Formula, the differential of the process f(X_t)=exp(γt)X_t is given by

![eq2](https://latex.codecogs.com/svg.image?df=\bigg[\frac{\partial&space;f}{\partial&space;t}-\gamma&space;X_t\frac{\partial&space;f}{\partial&space;x}&plus;\frac{\sigma^2}{2}\frac{\partial^2&space;F}{\partial&space;x^2}\bigg]dt&plus;\sigma\frac{\partial&space;f}{\partial&space;x}dW_t&space;)

which gives,

![eq3](https://latex.codecogs.com/svg.image?\bigg[\gamma&space;e^{\gamma&space;t}X_t&plus;(-\gamma&space;X_t)e^{\gamma&space;t}&plus;0\bigg]dt&plus;\sigma&space;e^{\gamma&space;t}dW_t=\sigma&space;e^{\gamma&space;t}dW_t)

Thanks to this simplification, we can see that the integrated process f (where the integral here is an Itô integral) is given by

![eq4](https://latex.codecogs.com/svg.image?e^{\gamma&space;t}X_t-X_0=\int_{0}^{t}\sigma&space;e^{\gamma&space;s}dW_s)

So that 

![eq5](https://latex.codecogs.com/svg.image?X_t=e^{-\gamma&space;t}X_0&plus;\int_{0}^{t}\sigma&space;e^{-\gamma(t-s)}dW_s)

In particular, we see that the second term on the R.H.S. is a Gaussian process (the integral of an deterministic process with a respect to a Wiener Process is Gaussian).
Thus if the initial distribution X_0 is gaussian, then it is clear that the Ornstein-Uhlenbeck process X_t is also gaussian. The mean remains stationary, and computing variances, we see that 

![eq6](https://latex.codecogs.com/svg.image?\mathbb{E}\bigg[\bigg(\sigma\int_{0}^{t}e^{-\gamma(t-s)}dW_s\bigg)^2\bigg]=\int_{0}^{t}e^{-2\gamma(t-s)}ds=\frac{1}{2\gamma}(1-e^{{\gamma(s-t)}})))

Which means that, scaling by a factor of σ^2

![eq7](https://latex.codecogs.com/svg.image?X_t\rightarrow&space;N\bigg(0,\frac{\sigma^2}{2\gamma}\bigg))

And if the initial distribution is also ~ N(0, σ^2/(2γ)), then X_t is stationary by choice of 
