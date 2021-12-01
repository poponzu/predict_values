#テーブルの結合のコード
join_data = pd.merge(items,item_categories[["item_category_name","item_category_id"]], on = "item_category_id",how = "left")
new_sales_train = pd.merge(sales_train,join_data[["item_id","item_category_id","item_category_name"]],on ="item_id",how = "left")

# dateをdatetime型に変換して、新しく["month”]列を作りました
train["date"] = pd.to_datetime(train["date"])
train["month"]=train["date"].dt.strftime("%Y%m")
train[["date","month"]].head()
