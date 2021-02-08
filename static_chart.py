import numpy as np
import matplotlib.pyplot as plt



def figure_2():


    dt = 0.01
    t = np.arange(-50, 50, dt) # przedział czasowy od 0 do 50 co 0,01



    # Two signals with a coherent part at 10Hz and a random part
    s1 = np.sin(2 * np.pi * 0.2 * t) # lista z elementami funkcji w przedziale t
    s2 = np.sin(2 * np.pi * 0.1 * t)

    s3 = -(pow((10 * t), 2)) + 500
    s4 = (10 * t)
    s5 = -(10 * t)

    fig, axs = plt.subplots(2, 1)  # ilosć wykresów
    fig.canvas.set_window_title('Nazwa okna z wykresami')

    axs[0].plot(t, s1, t, s2)
    axs[0].set_title('funkcje s1 i s2')
    axs[0].set_xlim(0, 50) # zakres
    axs[0].set_xlabel('time')
    axs[0].set_ylabel('s1 and s2')
    axs[0].grid(True)

    axs[1].plot(t, s3, t, s4, t, s5) # dowolna ilość funkcji
    axs[1].set_title('funkcje s3, s4 i s5')
    axs[1].set_xlim(-20, 20)
    axs[1].set_ylim(-600, 600)
    axs[1].set_xlabel('time')
    axs[1].set_ylabel('s3')
    axs[1].grid(True)




    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    figure_2()