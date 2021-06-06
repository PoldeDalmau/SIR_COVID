def integrate(I, gamma, ts, dt):
    It = np.asarray(I)
    integral = gamma*np.sum(It[ts:]*dt)
    return integral