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
Thus if the initial distribution X_0 is gaussian, then it is clear that the Ornstein-Uhlenbeck process X_t is also gaussian [1]. The mean remains stationary, and computing variances, we see that 

![eq6](https://latex.codecogs.com/svg.image?\mathbb{E}\bigg[\bigg(\int_{0}^{t}e^{-\gamma(t-s)}dW_s\bigg)^2\bigg]=\int_{0}^{t}e^{-2\gamma(t-s)}ds=\frac{1}{2\gamma}(1-e^{{\gamma(s-t)}}))

Which means that, scaling by a factor of σ^2

![eq7](https://latex.codecogs.com/svg.image?X_t\rightarrow&space;N\bigg(0,\frac{\sigma^2}{2\gamma}\bigg)\quad\text{as}\quad&space;t\rightarrow\infty)

And if the initial distribution is also ~ N(0, σ^2/(2γ)), then X_t is stationary by what follows...

3. The O-U Process is Markovian

This third property follows from what we have established in the previous explicit solution to the SDE defining the O-U process, namely that the the O.U. process is given as 

![eq5](https://latex.codecogs.com/svg.image?X_t=e^{-\gamma&space;t}X_0&plus;\int_{0}^{t}\sigma&space;e^{-\gamma(t-s)}dW_s\quad (5))

To show a process is markovian, it suffices to prove it for a fixed initial state x_0=0, in which case the process reduces to:

![eq8](https://latex.codecogs.com/svg.image?X_t=\int_{0}^{t}\sigma&space;e^{-\gamma(t-s)}dW_s\quad (5))

And then by applying the same approach as used above, we can see that the covariance of X_t and X_(t-s) can be calculated as 

![eq9](https://latex.codecogs.com/svg.image?e^{-\mu&space;s}\frac{\sigma^2}{2\mu})

Which can then be used to show that

![eq10](https://latex.codecogs.com/svg.image?\frac{Cov(X_s,X_r)Cov(X_r,X_t)}{Cov(X_r,X_r)})

A neccesary and sufficient condition for a Gaussian Process to be Markovian [2]. Seeing as the O-U process, at least with these parameters, is Markovian, the fact that it is stationary corresponds with the case when X_0 is set to the stationary distribution above: N(0, σ^2/(2γ))

On the computational side of things, we can see that the Euler Maruyama scheme provides sample results that converge to samples of the hypothetical O-U continuous process, which can be seen by increaing the value of the N parameter in the beginning of process.py, which controls samples/interval.

N=40:

![Process_0 5_1_1_1_40_steps](https://github.com/blawton/ornstein_uhlenbeck/assets/46683509/00146f5b-4c2d-4e83-aadd-1e3891685182)

N=400:

![Process_0 5_1_1_1_400_steps](https://github.com/blawton/ornstein_uhlenbeck/assets/46683509/37878366-b723-4eab-88ba-7d8e1fd23629)

In the case where we start with a value of y_0 different from μ, we can see that controlling the value of γ controls how fast reversion to the mean happens.

y_0=2, μ=1, γ=.5, σ=2:

![Process_0 5_2_1_5_400_steps](https://github.com/blawton/ornstein_uhlenbeck/assets/46683509/f439a069-1dd8-42fe-b407-b48941ca380d)

y_0=2, μ=1, γ=2, σ=2:

![Process_2_2_1_5_400_steps](https://github.com/blawton/ornstein_uhlenbeck/assets/46683509/16c553a2-5431-43e9-a995-b3a39255c872)

In this regard, we finally note that the Ornstein_Uhlenbeck Process is the continuous time analogue to an AR(1) process in the same way that a Wiener Process is the continuous analogue to a random walk. The Euler-Maruyam scheme gives us a way to model this discrete-time approximation.

Citations:

1. E, W., Li, T., & Vanden-Eijnden, E. (2019). Applied Stochastic Analysis (pp. 152-153). American Mathematical Society.

2. Marcus, M., & Rosen, J. (2006). Markov Processes, Gaussian Processes, and Local Times (pp. 201-202). Cambridge University Press.
