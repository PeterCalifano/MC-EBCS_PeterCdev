import subprocess
import platform

# Select the PBRT executable based on OS
if platform.system() == "Windows":
    pbrt_path = ".\\build\\Release\\pbrt.exe"
else:
    pbrt_path = "./build/pbrt"

# Define commands to run
commands = [
    # baseline
    f"{pbrt_path} --spp 4096 --threshold 3.0 --uniform ./scenes/LivingRoom/",
    f"{pbrt_path} --spp 4096 --threshold 0.6 --uniform ./scenes/SanMiguel/",
    f"{pbrt_path} --spp 4096 --threshold 0.5 --uniform ./scenes/TwoBoxes",
    f"{pbrt_path} --spp 4096 --threshold 0.5 --uniform ./scenes/Cupofwater/",

    # ours
    f"{pbrt_path} --spp 4096 --threshold 3.0 ./scenes/LivingRoom/",
    f"{pbrt_path} --spp 4096 --threshold 0.6 ./scenes/SanMiguel/",
    f"{pbrt_path} --spp 4096 --threshold 0.5 ./scenes/TwoBoxes",
    f"{pbrt_path} --spp 4096 --threshold 0.5 ./scenes/Cupofwater/"
]

# Execute each command
for command in commands:
    subprocess.run(command, shell=True, check=True)
