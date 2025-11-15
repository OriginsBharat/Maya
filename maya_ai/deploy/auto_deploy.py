import sys
import os

def check_python():
    """Check if Python is installed"""
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def create_directories():
    """Create needed directories"""
    dirs = ['colab', 'core', 'config']
    for directory in dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✅ Created directory: {directory}")
    return True

def deploy_to_colab():
    """Deploy brain to Google Colab"""
    print("\n📓 Setting up Google Colab...")
    print("1. Upload maya_brain.ipynb to Google Colab")
    print("2. Run all cells")
    print("3. Copy the Gradio public URL")
    print("✅ Brain will stay active for 12 hours")

def main():
    print("Starting Maya deployment...")
    check_python()
    create_directories()
    deploy_to_colab()
    print("\n✅ Ready for next step")

if __name__ == "__main__":
    main()
