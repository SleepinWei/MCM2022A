import matplotlib.pyplot as plt 

plt.style.use("bmh")
t = [3989.782954,3967.707036,3962.324778,3956.996913,3951.723282,3946.503732,3941.338106,3916.313195]
x = [5.3,5.7,5.8,5.9,6,6.1,6.2,6.7] 
print((x[-1]-x[0])/3956)
print((3953.54-3954.91)/3951.72 / (46.5-47.5) * 47)

plt.plot(x,t,label="t",marker="o")
plt.title("v_w - t")
plt.xlabel("v_w")
plt.ylabel("t")
plt.legend()
plt.show()