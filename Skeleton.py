def deriv(y, t, N, beta, gamma):
    """The SIR model differential equations.
    """
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

def deriv2pop(y, t, beta, eta):
    """SIR for two populations"""
    S_1, S_2, I_1, I_2, R_1, R_2 = y
    
    beta11 = beta[0][0]
    beta12 = beta[0][1]
    beta21 = beta[1][0]
    beta22 = beta[1][1]

    
    eta1 = eta[0][0]
    eta2 = eta[1][1]
    
    dS1dt = -S_1 * (beta11 * I_1 + beta12 * I_2)
    dS2dt = -S_2 * (beta21 * I_1 + beta22 * I_2)
    
    dI1dt = S_1 * (beta11 * I_1 + beta12 * I_2) - eta1 * I_1
    dI2dt = S_2 * (beta21 * I_1 + beta22 * I_2) - eta2 * I_2
    
    dR1dt = eta1 * I_1
    dR2dt = eta2 * I_2
    
    return dS1dt, dS2dt, dI1dt, dI2dt, dR1dt, dR2dt
    
    
def plot(S,I,R):
    # Plot the data on three separate curves for S(t), I(t) and R(t)
    fig = plt.figure(facecolor='w')
    ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
    ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
    ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Active Infections')
    ax.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Removed')
    #ax.plot(t, dIdt/1000, 'y', alpha=0.5, lw=2, label='Newly Infected')    
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
    
    