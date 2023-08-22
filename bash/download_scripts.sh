echo "Downloading scripts from arctic"
git clone https://github.com/zc-alexfan/arctic.git
mkdir -p common
cd arctic/common
cp body_models.py mesh.py rot.py torch_utils.py ld_utils.py object_tensors.py thing.py xdict.py ../../common/
cd ../..
rm -rf arctic/