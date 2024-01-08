import gradio as gr
import pickle
default_dict = {
    'MSSubClass' : 60,'MSZoning' : 'RL','LotArea' : 5000,'Street' : 'Pave'
    ,'LotShape' : 'Reg','LandContour' : 'Lvl','Utilities' : 'AllPub','LotConfig' : 'Inside'
    ,'LandSlope' : 'Gtl','Neighborhood' : 'CollgCr','Condition1' : 'Norm','BldgType' : '1Fam'
    ,'HouseStyle' : '2Story','OverallQual' : 7,'OverallCond' : 8,'YearBuilt' : 1965,'YearRemodAdd' : 2003
    ,'RoofStyle' : 'Gable','RoofMatl' : 'CompShg','Exterior1st' : 'VinylSd','Exterior2nd' : 'VinylSd',
    'ExterQual' : 'Gd','ExterCond' : 'TA','Foundation' : 'PConc','BsmtFinSF1' : 578,'BsmtFinSF2' : 668,
    'BsmtUnfSF' : 434 ,'HeatingQC' : 'Ex','CentralAir' : 'Y','1stFlrSF' : 1022,'2ndFlrSF' : 756,
    'LowQualFinSF'  : 513,'GrLivArea' : 1262,'BsmtFullBath' : 1,'BsmtHalfBath' : 1,'FullBath' : 2,
    'HalfBath' : 1,'BedroomAbvGr' : 3,'KitchenAbvGr' : 2,'KitchenQual' : 'Gd','TotRmsAbvGrd' : 9,
    'Functional' : 'Typ','Fireplaces' : 1,'GarageArea' : 548,'PavedDrive' : 'Y','WoodDeckSF' : 298,
    'OpenPorchSF' : 213,'EnclosedPorch' : 272,'3SsnPorch' : 320,'ScreenPorch' : 410,'PoolArea' : 648,
    'MiscVal' : 8300,'YrSold' : 2005
}


def greet(*args):
    kekboost_model = None
    with open("models\kekboost.pickle", "rb") as file:
        kekboost_model = pickle.load(file)
    print([args])
    vec = []
    
    if sum([0 if (x == [] or x == '') else 1 for x in args]) != 53:
        print(sum([0 if (x == [] or x == '') else 1 for x in args]))
        vec = [list(default_dict.values())]
    else:
        for i in args:
            try:
                t = int(i)
                vec.append(t)
            except:
                vec.append(i)
        vec = [vec]

    print(vec)
    res = kekboost_model.predict(vec)
    
    return res[0] #"Hello " * intensity + name + "!"

demo = gr.Interface(
    fn=greet,
    inputs=[
    gr.Dropdown(
        [60, 20, 70, 50, 190, 45, 90, 120, 30, 85, 80, 160, 75, 180, 40], label="Класс здания"
    )  
    , gr.Dropdown(
        ['RL', 'RM', 'C (all)', 'FV', 'RH'], label="Классификация зонирования"
    ) 
    , gr.Textbox(label="Размер участка") 
    , gr.Dropdown(
        ['Pave', 'Grvl'], label="Улица"
    ) 
    , gr.Dropdown(
        ['Reg', 'IR1', 'IR2', 'IR3'], label="Форма объекта недвижимости", 
    )
    , gr.Dropdown(
        ['Lvl', 'Bnk', 'Low', 'HLS'], label="Ровность участка"
    )
    , gr.Dropdown(
        ['AllPub', 'NoSeWa'], label="Утилиты"
    )
    , gr.Dropdown(
        ['Inside', 'FR2', 'Corner', 'CulDSac', 'FR3'], label="Конфигурация лота"
    )
    , gr.Dropdown(
        ['Gtl', 'Mod', 'Sev'], label="Уклон участка"
    )
    , gr.Dropdown(
        ['CollgCr', 'Veenker', 'Crawfor', 'NoRidge', 'Mitchel', 'Somerst', 'NWAmes', 'OldTown', 'BrkSide', 'Sawyer', 'NridgHt', 'NAmes', 'SawyerW', 'IDOTRR', 'MeadowV', 'Edwards', 'Timber', 'Gilbert', 'StoneBr', 'ClearCr', 'NPkVill', 'Blmngtn', 'BrDale', 'SWISU', 'Blueste'], label="Физические местоположения в пределах города Эймс"
    )
    , gr.Dropdown(
        ['Norm', 'Feedr', 'PosN', 'Artery', 'RRAe', 'RRNn', 'RRAn', 'PosA', 'RRNe'], label="Близость к автомобильной и железной дороге"
    )
    , gr.Dropdown(
        ['1Fam', '2fmCon', 'Duplex', 'TwnhsE', 'Twnhs'], label="Тип жилья"
    )
    , gr.Dropdown(
        ['2Story', '1Story', '1.5Fin', '1.5Unf', 'SFoyer', 'SLvl', '2.5Unf', '2.5Fin'], label="Стиль жилья"
    )
    , gr.Textbox(label="общее качество материала и отделки", info="1..10") 
    , gr.Textbox(label="общая оценка состояния", info="1..10") 
    , gr.Textbox(label="год строительства", info="1900..2020")
    , gr.Textbox(label="год реставрации", info="1900..2020")
    , gr.Dropdown(
        ['Gable', 'Hip', 'Gambrel', 'Mansard', 'Flat', 'Shed'], label="Тип крыши"
    )
    , gr.Dropdown(
        ['CompShg', 'WdShngl', 'Metal', 'WdShake', 'Membran', 'Tar&Grv', 'Roll', 'ClyTile'], label="Материал крыши"
    )
    , gr.Dropdown(
        ['VinylSd', 'MetalSd', 'Wd Sdng', 'HdBoard', 'BrkFace', 'WdShing', 'CemntBd', 'Plywood', 'AsbShng', 'Stucco', 'BrkComm', 'AsphShn', 'Stone', 'ImStucc', 'CBlock'], label="Наружное покрытие дома"
    )
    , gr.Dropdown(
        ['VinylSd', 'MetalSd', 'Wd Shng', 'HdBoard', 'Plywood', 'Wd Sdng', 'CmentBd', 'BrkFace', 'Stucco', 'AsbShng', 'Brk Cmn', 'ImStucc', 'AsphShn', 'Stone', 'Other', 'CBlock'], label="Наружное покрытие дома (если более одного материала)"
    )
    , gr.Dropdown(
        ['Gd', 'TA', 'Ex', 'Fa'], label="Качество материала экстерьера"
    )
    , gr.Dropdown(
        ['TA', 'Gd', 'Fa', 'Po', 'Ex'], label="Текущее состояние материала снаружи"
    )
    , gr.Dropdown(
        ['PConc', 'CBlock', 'BrkTil', 'Wood', 'Slab', 'Stone'], label="Тип фундамента"
    )
    , gr.Textbox(label="готовые квадратные футы типа 1", info="0..2200") 
    , gr.Textbox(label="готовые квадратные футы типа 2", info="0..2200") 
    , gr.Textbox(label="незаконченные квадратные футы подвала", info="0..2200") 
    , gr.Dropdown(
        ['Ex', 'Gd', 'TA', 'Fa', 'Po'], label="Качество и состояние отопления"
    )
    , gr.Dropdown(
        ['Y', 'N'], label="Центральное кондиционирование"
    )
    , gr.Textbox(label="квадратные футы первого этажа", info="0..5000") 
    , gr.Textbox(label="квадратные футы второго этажа", info="0..5000") 
    , gr.Textbox(label="квадратные футы с отделкой низкого качества (все этажи)", info="0..5000")
    , gr.Textbox(label="жилая площадь над землей, квадратные футы", info="0..5000")  
    , gr.Textbox(label="Полностью оборудованные ванные комнаты в подвале", info="0..3") 
    , gr.Textbox(label="Полуванные комнаты в подвале", info="0..2") 
    , gr.Textbox(label="полностью оборудованные ванные комнаты над уровнем моря", info="0..3")
    , gr.Textbox(label="полуванны выше уровня", info="0..2")
    , gr.Textbox(label="Количество спален над цокольным этажом", info="0..10")
    , gr.Textbox(label="Количество кухонь", info="0..5")
    , gr.Dropdown(
        ['Gd', 'TA', 'Ex', 'Fa'], label="Качество кухни"
    )
    , gr.Textbox(label="общее количество комнат выше уровня (без ванных комнат)", info="0..25")
    , gr.Dropdown(
        ['Typ', 'Min1', 'Maj1', 'Min2', 'Mod', 'Maj2', 'Sev'], label="Рейтинг функциональности дома"
    )
    , gr.Textbox(label="Количество каминов", info="0..5")
    , gr.Textbox(label="Размер гаража в квадратных футах", info="0..1000")
    , gr.Dropdown(
        ['Y', 'N', 'P'], label="Асфальтированная подъездная дорога"
    )
    , gr.Textbox(label="Площадь деревянного настила в квадратных футах", info="0..1000")
    , gr.Textbox(label="площадь открытой веранды в квадратных футах", info="0..1000")
    , gr.Textbox(label="площадь крытой веранды в квадратных футах", info="0..1000")
    , gr.Textbox(label="Трехсезонная веранда в квадратных футах", info="0..1000")
    , gr.Textbox(label="площадь веранды в квадратных футах", info="0..1000")
    , gr.Textbox(label="площадь бассейна в квадратных футах", info="0..1000")
    , gr.Textbox(label="Значение различных дополнительных функций", info="0..10000")
    , gr.Textbox(label="Год продажи", info="2005..2010")

],
    outputs=[gr.Textbox(label="Предполагаемая стоимость Вашего дома")],
)
demo.language = "en"
demo.launch()
# to see your result you should go to browser and write http://127.0.0.1:7860

# linearModel = None
# with open("LinearRegression.pickle", "rb") as file:
#     linearModel = pickle.load(file)