仿真运行方式：打开工程，直接运行examples\dqn_cartpole.py
串行模型/并行模型切换：在Version Control toolbar里，切换branch。其中，old代表串行模型，new代表并行模型。
模型参数调节：在.\h_generation_based_on_traffic.py里，我将参数的定义集中在Traffic > __init__()中。参数被分为路段参数、车辆移动模型参数等参数组，可相应调节。

文件结构：
example\
	dqn_cartpole.py：主文件，运行该文件可开启仿真，得到训练完成的网络和训练历史文件
	network_test.py：可测试网络性能，得出多种数据
	plot.py、plot_convergence：收敛图绘制
	plot_delay.py：时延图绘制
	plot_use_rate.py：时间利用率绘制
	plot_bars：性能对比图绘制
	pure_v2v_v2i_test：baseline schemes性能仿真
network_parameter\:存放训练完成的网络文件
history_plot\:存放训练历史文件
h_generation_based_on_traffic.py:MEC网络模型
