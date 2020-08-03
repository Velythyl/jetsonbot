until apt-get update; do sleep 2; done

mkdir data && cd data
mkdir config && cd config
mkdir calibrations && cd calibrations
mkdir camera_extrinsic && cd camera_extrinsic && echo "homography: [-4.89775e-05, -0.0002150858, -0.1818273, 0.00099274, 1.202336e-06, -0.3280241, -0.0004281805, -0.007185673, 1]" > default.yaml
cd -
mkdir camera_intrinsic && cd camera_intrinsic && echo "image_width: 640
image_height: 480
camera_name: /porsche911/rosberrypi_cam
camera_matrix:
  rows: 3
  cols: 3
  data: [307.7379294605756, 0, 329.692367951685, 0, 314.9827773443905, 244.4605588877848, 0, 0, 1]
distortion_model: plumb_bob
distortion_coefficients:
  rows: 1
  cols: 5
  data: [-0.2565888993516047, 0.04481160508242147, -0.00505275149956019, 0.001308569367976665, 0]
rectification_matrix:
  rows: 3
  cols: 3
  data: [1, 0, 0, 0, 1, 0, 0, 0, 1]
projection_matrix:
  rows: 3
  cols: 4
  data: [210.1107940673828, 0, 327.2577820024981, 0, 0, 253.8408660888672, 239.9969353923052, 0, 0, 0, 1, 0]" > default.yaml
cd -
mkdir kinematics && cd kinematics && echo "baseline: 0.1
gain: 1.0
k: 27.0
limit: 1.0
radius: 0.0318
trim: 0.0" > default.yaml