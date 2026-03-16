import pandas as pd
from sklearn.model_selection import train_test_split

def make_splits(df, seed=42):

    train, temp = train_test_split(
        df,
        test_size=0.2,
        stratify=df["label"],
        random_state=seed
    )

    val, test = train_test_split(
        temp,
        test_size=0.5,
        stratify=temp["label"],
        random_state=seed
    )

    return {
        "train":train,
        "val":val,
        "test":test
    }


def save_splits(splits,out_dir):

    splits["train"]["text_id"].to_csv(f"{out_dir}/splits_train_ids.txt",index=False)
    splits["val"]["text_id"].to_csv(f"{out_dir}/splits_val_ids.txt",index=False)
    splits["test"]["text_id"].to_csv(f"{out_dir}/splits_test_ids.txt",index=False)