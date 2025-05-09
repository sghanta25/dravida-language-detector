import fasttext
model = fasttext.train_supervised(
    input="translit_train.txt",
    epoch=35,
    lr=1.0,
    wordNgrams=2,
    minn=2,           
    maxn=5,          
    verbose=2
)
model.save_model("language_detector/translit_model.ftz")
print("Model trained and saved ✅")
