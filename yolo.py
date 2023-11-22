#!/usr/bin/env python3

# yolo.py

import os

def convert_to_yolo(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            # 각 행에서 필요한 데이터 추출 (입력 형식에 따라 수정이 필요할 수 있음)
            data = line.strip().split()  # 예: 공백으로 구분된 경우
            object_class = data[0]
            x_center = float(data[1])
            y_center = float(data[2])
            width = float(data[3])
            height = float(data[4])

            # YOLO 형식으로 변환하여 출력 파일에 쓰기
            yolo_format_line = f"{object_class} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n"
            output_file.write(yolo_format_line)

if __name__ == "__main__":
    # 입력 디렉토리
    input_directory = '/home/a/uk.v1-uk.yolov5pytorch/train/labels'

    # 출력 디렉토리
    output_directory = '/home/a/uk.v1-uk.yolov5pytorch/train/hello'

    # 모든 .txt 파일에 대해 작업 수행
    for file_name in os.listdir(input_directory):
        if file_name.endswith(".txt"):
            input_file_path = os.path.join(input_directory, file_name)
            output_file_path = os.path.join(output_directory, file_name)

            convert_to_yolo(input_file_path, output_file_path)
            print(f"Conversion complete. Output saved to {output_file_path}")

