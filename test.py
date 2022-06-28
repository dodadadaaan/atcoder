import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp 
import os
import time

from util import (
    mu,
    compute_Lagrange,
    compute_dU_bar,
    Energy,
    pcr3bp_phi,
    lyap_init,
    event_y0mp,
    event_y0pm
)

def diff_corr():

def contination():
    

def main():
    t1 = time.time()
    #ラグランジュ点の座標
    L = compute_Lagrange()
    E = [-1.59, -1.57, -1.55, -1.53, -1.51]
    colors = ['blue', 'cyan', 'green', 'red', 'gold']
    ans = list()
    #グラフの設定
    fig = plt.figure()
    ax = fig.add_subplot()
    for i in range(5):
        x1 = contination(L[0][0], E[i])
        x2 = contination(L[0][1], E[i])
        line1 = solve_ivp(pcr3bp_phi, [0,100], x1, events=event_y0mp,rtol = 1e-12, atol = 1e-12)
        line2 = solve_ivp(pcr3bp_phi, [0,100], x2, events=event_y0pm,rtol = 1e-12, atol = 1e-12)
        ans.append(line1.t[-1]/np.pi)
        ax.plot(line1.y[0], line1.y[1], color=colors[i], label=f'E:{E[i]}')
        ax.plot(line2.y[0], line2.y[1], color=colors[i])
        
    ax.plot(L[0][:2],L[1][:2],'kX')
    ax.set_xlabel('$\it{x}$',fontsize=25,fontstyle='italic')
    ax.set_ylabel('y',fontsize=25)
    fig.gca().set_aspect('equal')
    ax.set_title('Lyapunov')
    plt.tight_layout()
    fig.legend()
    #グラフの保存
    fig.savefig(os.path.dirname(__file__)+"\Lyapunov.png")

    t2 = time.time()
    print(ans)
    print(f'経過時間:{t2-t1}s')
    plt.show()

if __name__=='__main__':
    main()