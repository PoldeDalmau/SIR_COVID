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
    ax.plot(t, S/N, 'b', alpha=0.5, lw=2, label='Susceptible')
    ax.plot(t, I/N, 'r', alpha=0.5, lw=2, label='Active Infections')
    ax.plot(t, R/N, 'g', alpha=0.5, lw=2, label='Removed')
    if u != 0:
        ax.plot(t, V/N, 'c', alpha=0.5, lw=2, label='Vaccinated')
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
    
    