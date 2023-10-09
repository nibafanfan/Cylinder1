# Cylinder1
Cylinder3D model on Rellis-3D dataset: training and visualization

Most of the time, it's crucial to calculate the appropriate trajectory for robots...
![image](https://github.com/nibafanfan/Cylinder1/assets/33424645/16dc4f6c-83ec-4ca6-823d-49063677ca9e)

Improve traversability estimation
![image](https://github.com/nibafanfan/Cylinder1/assets/33424645/2f5665ed-7638-47b9-b91a-7c773a2f9ef1)

Basic info
output_shape:
    - 480
    - 360
    - 32

  fea_dim: 9
  out_fea_dim: 256
  num_class: 15
  num_input_features: 16
  use_norm: True
 
  init_size: 32
  checkpoint_every_n_steps: 4000
  max_num_epochs: 40
  eval_every_n_steps: 4000
  learning_rate: 0.001
  train:
    - 0
    - 1
    - 2
   
  valid:
    - 3
  test:
    - 4
![image](https://github.com/nibafanfan/Cylinder1/assets/33424645/205df09c-4312-41d5-911c-a211ae260547)

![image](https://github.com/nibafanfan/Cylinder1/assets/33424645/b6b3049e-eafb-4d72-9e7c-b436266f9113)



![image](https://github.com/nibafanfan/Cylinder1/assets/33424645/5559415d-74c0-414c-8794-c1d00038d089)

