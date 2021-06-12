def deriv(y, t, beta, gamma):
    """
    The SIR model differential equations for one population.
    Parameters
    ------------------------------------
    y: vector
        vector where the number of S (susceptible), I (infected) and R (recovered) are stored
    t:
        grid of time points (in days)
    beta: float
        contact rate of the disease. An infected individual comes into contact with beta*N individuals per unit time
    gamma: float
        mean recovery rate. 1/gamma is the average duration of the disease (in days)
    Returns
    -----------------------------------
    dSdt: float
        Differential equation for the change in susceptible individuals
    dIdt: float
        Differential equation for the change in infected individuals
    dRdt: float
        Differential equation for the change in recovered individuals
    """
    S, I, R, V = y
    if S > 0:
        dSdt = -beta * S * I / N - alpha*u
        dVdt = alpha*u
    else:
        dSdt = -beta * S * I / N
        dVdt = 0
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    
    return dSdt, dIdt, dRdt, dVdt

def deriv_new(y, t, beta, gamma):
    """
    The SIR model differential equations for one population.
    Parameters
    ------------------------------------
    y: vector
        vector where the number of S (susceptible), I (infected) and R (recovered) are stored
    t:
        grid of time points (in days)
    beta: float
        contact rate of the disease. An infected individual comes into contact with beta*N individuals per unit time
    gamma: float
        mean recovery rate. 1/gamma is the average duration of the disease (in days)
    Returns
    -----------------------------------
    dSdt: float
        Differential equation for the change in susceptible individuals
    dIdt: float
        Differential equation for the change in infected individuals
    dRdt: float
        Differential equation for the change in recovered individuals
    """
    S, I, R, V = y
    if S > 0:
        dSdt = -beta * S * I / N - alpha[i]*u[i]
        dVdt = alpha[i]*u[i]
    else:
        dSdt = -beta * S * I / N
        dVdt = 0
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    
    return dSdt, dIdt, dRdt, dVdt

def deriv2pop(y, t, beta, gamma):
    """
    The SIR model differential equations for two populations.
    Parameters
    ------------------------------------
    y: tuple
        tuple where the number of S (susceptible), I (infected) and R (recovered) are stored
    t:
        grid of time points (in days)
    beta: float
        contact rate of the disease. An infected individual comes into contact with beta*N individuals per unit time
    gamma: float
        mean recovery rate. 1/gamma is the average duration of the disease (in days)
    Returns
    -----------------------------------
    dS1dt: float
        Differential equation for the change in susceptible individuals in population 1
    dS2dt: float
        Differential equation for the change in susceptible individuals in population 2
    dI1dt: float
        Differential equation for the change in infected individuals in population 1
    dI2dt: float
        Differential equation for the change in infected individuals in population 2
    dR1dt: float
        Differential equation for the change in recovered individuals in population 1
    dR2dt: float
        Differential equation for the change in recovered individuals in population 2
    """
    S_1, S_2, I_1, I_2, R_1, R_2 = y
    
    beta11 = beta[0][0]              # beta in population 1
    beta12 = beta[0][1]              # beta that determines the influence of population 2 on population 1
    beta21 = beta[1][0]              # beta that determines the influence of population 1 on population 2
    beta22 = beta[1][1]              # beta in population 2

    
    gamma1 = gamma[0][0]              # gamma in population 1
    gamma2 = gamma[1][1]              # gamma in population 2
    
    dS1dt = -S_1/N1 * (beta11 * I_1 + beta12 * I_2)
    dS2dt = -S_2/N2 * (beta21 * I_1 + beta22 * I_2)
    
    dI1dt = S_1/N1 * (beta11 * I_1 + beta12 * I_2) - gamma1 * I_1
    dI2dt = S_2/N2 * (beta21 * I_1 + beta22 * I_2) - gamma2 * I_2
    
    dR1dt = gamma1 * I_1
    dR2dt = gamma2 * I_2
    
    return dS1dt, dS2dt, dI1dt, dI2dt, dR1dt, dR2dt
    
def derivnpop(y, t, beta, gamma):
    """The SIR model differential equations for two populations.
    Parameters
    ------------------------------------
    y: tuple
        tuple where the number of S (susceptible), I (infected) and R (recovered) are stored
    t:
        grid of time points (in days)
    beta: float
        contact rate of the disease. An infected individual comes into contact with beta*N individuals per unit time
    gamma: float
        mean recovery rate. 1/gamma is the average duration of the disease (in days)
    Returns
    -----------------------------------
    *dSdt, *dIdt, *dRdt: tuple
        Rate of change of Susceptibles, Infected and Recovered for each population at time t and y.
    """
    S = np.array(y[:2])      # 2 is the number of populations
    I = np.array(y[2:2*2])
    R = np.array(y[-2:])
    
    dSdt = -(S/N)*(beta.dot(I))
    dIdt =  S/N*(beta.dot(I)) - gamma.dot(I)
    dRdt =  gamma.dot(I)
    
    return *dSdt, *dIdt, *dRdt

def plot(S,I,R):
    # Plot the data on three separate curves for S(t), I(t) and R(t)
    fig = plt.figure(facecolor='w')
    ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
    ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
    ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Active Infections')
    ax.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Removed')
    if u != 0:
        ax.plot(t, V/1000, 'c', alpha=0.5, lw=2, label='Vaccinated')
    #ax.plot(t, beta*S*I/N**2, 'y', alpha=0.5, lw=2, label='Newly Infected')    
    ax.set_xlabel('Time /days')
    ax.set_ylabel('Number (1000s)')
    #ax.set_ylim(0,1.1)
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    for spine in ('top', 'right', 'bottom', 'left'):
        ax.spines[spine].set_visible(False)
    plt.show()
    
def integrate(I):
    time = np.arange(0,len(I))
    integral = np.zeros(len(time))
    for i in time:
        integral[i] = np.trapz(I[:i], x = time[:i])
    return integral

def Canada_init(place):
    """Uses pandas to extract data for canada."""
    condition = df['prname'] == place
    Place = df[condition]
    t_ont = Place.date
    t_ont = t_ont.tolist()

    # Define populations
    rem_ont = Place.numdeaths + Place.numrecover
    rem_ont = rem_ont.tolist()
    act_ont = Place.numactive
    act_ont = act_ont.tolist()
    act_ont = np.array(act_ont[start:end])
    Susc = N - act_ont - np.array(rem_ont[start:end])
    Rem = np.array(rem_ont[start:end])
    #print('t start', t_ont[start], '\nt end', t_ont[end])
    return Rem, act_ont, Susc, t_ont

def R_0calculator(Susc):
    """Calculates R_0 and error"""
    lhs1 = np.log(Susc / Susc[0])
    rhs1 = Rem

    res = stats.linregress(rhs1, lhs1)
    #print(res.intercept*N/Rem[0])
    R_0 = -res.slope*N
    tinv = lambda p, df: abs(t.ppf(p/2, df))
    ts = tinv(0.05, len(rhs1)-2)

    textR_0 = str((f"{-N*res.slope:.6f} ± {N*ts*res.stderr:.6f}"))
    R_0err = N*ts*res.stderr
    #print("R_0 = " + textR_0)
    
    return lhs1, rhs1, R_0, R_0err, textR_0, res

def gammacalculator(Rem, Infec):
    """Calculate gamma and error"""
    lhs2 = np.array(Rem)
    rhs2 = integrate(Infec)
    res2 = stats.linregress(rhs2, lhs2)
    gamma = res2.slope
    tinv2 = lambda p, df: abs(t.ppf(p/2, df))
    ts2 = tinv2(0.05, len(rhs2)-2)

    textgamma = str((f"{res2.slope:.6f} ± {ts2*res2.stderr:.6f}"))
    gammaerr = ts2*res2.stderr

    #print("gamma =", textgamma)
    
    return lhs2, rhs2, gamma, gammaerr, textgamma, res2


def plotdataandfits():
    """Plot all relevant data and fits"""
    
    # Plot removed and infected

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6)) 
    date_form = DateFormatter('%b-%d')

    ax1.xaxis.set_major_formatter(date_form)
    ax1.scatter(np.array(t_ont[start:end]),np.array(Rem)/1e5, marker='.', label = "Real Data", facecolors='none', edgecolors='k', linewidths=0.5,)
    ax1.set_ylabel('Removed $R(t)$ in $10^5$', fontsize=13)
    ax1.plot(t_ont[start:end], R_model/1e5, label = "Fitted Model", c = 'b')
    ax1.plot(t_ont[start:end], R_model1/1e5, label = "Confidence Interval", c = 'b', linestyle = '--')
    ax1.plot(t_ont[start:end], R_model2/1e5, c = 'b', linestyle = '--')
    ax1.set_title(place+" 2020", fontsize=13)
    ax1.legend(fontsize = 13)

    ax2.xaxis.set_major_formatter(date_form)
    ax2.scatter(t_ont[start:end],np.array(Infec)/1e4, marker='.', label = "Real Data", facecolors='none', edgecolors='k', linewidths=0.5,) 
    ax2.set_ylabel('Infected $I(t)$ in $10^{4}$', fontsize=13)
    ax2.set_title(place+" 2020", fontsize=13)
    ax2.plot(t_ont[start:end], I_model/1e4, label = "Fitted Model", c = 'b')
    ax2.plot(t_ont[start:end], I_model1/1e4, label = "Confidence Interval", c = 'b', linestyle = '--')
    ax2.plot(t_ont[start:end], I_model2/1e4, c = 'b', linestyle = '--')
    ax2.legend(fontsize = 13)

    plt.show()

    #Plot data from which R_0 and gamma are obtained

    fig, (ax3, ax4) = plt.subplots(1, 2, figsize=(12,6)) 
    ax3.scatter(rhs1/1e5, lhs1/1e-3, facecolors='none', edgecolors='k', linewidths=0.5,label = "Real Data")
    ax3.set_xlabel("$R(t)$ in $10^5$", fontsize=13)
    ax3.set_ylabel("$\log(S(t)/S(t_0))$ in $10^{-3}$", fontsize=13)
    ax3.plot(rhs1/1e5, (res.slope*rhs1+res.intercept)/1e-3, c = 'b', label = "Fitted Model")
    #props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax3.text(0.05, 0.1, r"$R_0 = $" +textR_0, transform=ax3.transAxes, fontsize=14, verticalalignment='top')
    ax3.legend(fontsize = 13)

    ax4.scatter(rhs2/1e6, lhs2/1e5, facecolors='none', edgecolors='k', linewidths=0.5,label = "Real Data")
    ax4.plot(rhs2/1e6, (gamma * rhs2 + res2.intercept)/1e5, c = 'b', label = "Fitted Model")
    #ax4.plot(rhs2/1e6, ((gamma+gammaerr) * rhs2 + (gammaintercept))/1e5, c = 'r', label = "Fitted Model", linestyle='dashed') #attempt at plotting confidence interval but it's too small...
    ax4.set_xlabel(r'$\int_{t_s}^t I(\tau) \mathrm{d}\tau$ in $10^6$', fontsize=13)
    ax4.set_ylabel('$R(t)$ in $10^5$', fontsize=13)
    ax4.text(1.5, 0.1, r"$\gamma = $" + textgamma, transform=ax3.transAxes, fontsize=14, verticalalignment='top')
    ax4.legend(fontsize=13)

    plt.show()