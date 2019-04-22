import re
import arabic_reshaper as ar
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from collections import Counter
from bidi.algorithm import get_display

# -------------------Importing Data----------------------
data = pd.read_csv(
    "/home/muhammad/Downloads/بررسی-وضعیت-شغلی-برنامه-نویسان-و-مدیر-سیستم_های-ایران-jadi.net-97-Responses-Form-Responses-1.csv",
     index_col=False
     )
# print(data)

# -------------------Change columns title to English-----------------------
columns = ['timestamp', 'age', 'gender', 'living_region', 'working_region', 'work_experience', 'last_educational_status', 
            'international_documents', 'hours_of_week_spending_on_learning', 'most_important_position_for_learning',
            'non_working_projects', 'books', 'programming_lang', 'programming_lang_for_learning', 'databases', 'desktop_os',
            'server_os', 'mobile', 'programin_envirment', 'ide_theme', 'source_control', 'technogly', 'most_useable_system',
            'tab_or_space', 'favorite_drink', 'wearing_style', 'body_change', 'life_style', 'music', 'relations', 'digital_devices',
            'working_field', 'company', 'emploies', 'salary', 'working_services', 'working_style', 'how_work', 'wage', 'satification', 'are_you_programmer_?']
data.columns = columns
# print(data.columns)

# -------------------Function for write persian correctly in plots---------------------
def persian_writing(wrong_words):
    correct_words = []
    for word in wrong_words:
        reshaped_value = ar.reshape(word)
        correct_words.append(get_display(reshaped_value))
    return(correct_words)

# -------------------Function for write persian and english correctly in plots---------------------
def persian_english(wrong_word):
    if re.search(r'[A-Z]', wrong_word, re.IGNORECASE):
        wrong_word = wrong_word
        return wrong_word
    else:
        reshaped_value = ar.reshape(wrong_word)
        wrong_word = get_display(reshaped_value)
        return wrong_word

# -------------------Function for pie ploting------------------------
def circle_ploting(Data, title=None, circle=False, wrong=False, labels=None, explode=None, explod=0):
    explodes = []
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    if explod:
        while range(0, explod):
            explodes.append(0.5)
    else:
        explodes = explode
    
    if wrong == True:
        labels = persian_writing(labels)  

    plot_figure = plt.figure()
    plt.pie(Data, labels=labels, autopct='%1.1f%%', shadow=True, colors=colors, pctdistance=0.85, explode=explodes)
    plot_figure.suptitle("{}" .format(title))
     
    if circle == True:
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.tight_layout()

    plt.pause(30)
    plot_figure.show()
    
# -------------------Function for bar ploting-------------------
def bar_plotting(Data, title=None, xlabel=None, ylabel=None):
    y_pos = np.arange(len(Data.keys()))
    
    plt.figure()
    plt.bar(y_pos, Data.values())
    plt.xticks(y_pos, Data.keys(), rotation='vertical')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    plt.show()

# -------------------Function for determine value and counts of a data set--------------------
def value_and_count(dataset, v_c):
    if v_c == "v":
        return dataset.value_counts().keys().tolist()
    elif v_c == "c":
        return dataset.value_counts().tolist()

# -------------------Function for determine name and data of a specific value----------------------
def name_and_data(serie, dataset, field, n_d=None):
    name_list = []
    data_list = []
    for name in value_and_count(serie, "v"):
        name_list.append(name)
        data_list.append(dataset[dataset[field] == name])
    if n_d == "n":
        return name_list
    elif n_d == "d":
        return data_list
    elif n_d == None:
        return dict(zip(name_list, data_list))

# -------------------Function for spliting raws of datasets---------------------
def split_raw(Dataset):
    words = []
    for raw in Dataset:
        for word in raw.split(", "):
            words.append(word)


if __name__ == "__main__":

# -------------------Number of men and women participate in this poll----------------------
    men = data[data["gender"] == "مرد"]
    women = data[data["gender"] == "زن"]
    men_women_other = [len(men), len(women), (len(data) - (len(men) + len(women)))]

    labels = ["مرد", "زن", "دیگر"]

    # print("{} men participate in this poll" .format(len(men)))
    # print("{} women participate in this poll" .format(len(women)))
    # print("{} of who participate in this poll don't say their gender" .format(len(data) - (len(men) + len(women))))

    # circle_ploting(men_women_other, title="Gender Percantage", wrong=True, labels=labels, explod=3)

# -------------------Salary and Wage----------------------
    men_salary = men["salary"]
    women_salary = women["salary"]

    men_wage = men["wage"]
    women_wage = women["wage"]

    # print(men_wage.value_counts())
    # print(women_wage.value_counts())

    # print(men_salary.value_counts())
    # print(women_salary.value_counts())

    explode = (0.05, 0.05, 0.05, 0.05, 0.5, 0.5, 0.5, 0.5)

    # circle_ploting(value_and_count(men_wage, "c"), title="Men's wage", wrong=True, labels=value_and_count(men_wage, "v"), explod=7)
    # circle_ploting(value_and_count(women_wage, "c"), title="Women's wage", wrong=True, labels=value_and_count(women_wage, "v"), explod=6)

    # circle_ploting(value_and_count(men_salary, "c"), title="Men's salary", wrong=True, labels=value_and_count(men_salary, "v"), explode=explode)
    # circle_ploting(value_and_count(women_salary, "c"), title="Women's salary", wrong=True, labels=value_and_count(women_salary, "v"), explode=explode)

    men_work_experience = men["work_experience"]
    women_work_experience = women["work_experience"]


    # for name, data in name_and_data(men_work_experience, men, "work_experience", n_d=None).items():   
    #     plt.figure()
    #     plt.plot(persian_writing(value_and_count(data["salary"], "v")), value_and_count(data["salary"], "c"), color='g')
        
    #     reshaped_value = ar.reshape(name)
    #     correct_name = get_display(reshaped_value)
    #     plt.title(correct_name)

    # plt.show()

    # for name, data in name_and_data(women_work_experience, women, "work_experience", n_d=None).items():
    #     plt.figure()
    #     plt.plot(persian_writing(value_and_count(data["salary"], "v")), value_and_count(data["salary"], "c"), color='r')

    #     reshaped_value = ar.reshape(name)
    #     correct_name = get_display(reshaped_value)
    #     plt.title(correct_name)

    # plt.show()

# -------------------counts of using Programming langs---------------------
    langs = []
    programming_lang = data["programming_lang"]

    for raw in programming_lang:
        if raw != "برنامه نویسی نمی‌کنم":
            for lang in raw.split(", "):
                langs.append(lang)

    langs_name = Counter(langs).keys()
    langs_count = Counter(langs).values()


    dict_of_names_and_counts = dict(zip(langs_name, langs_count))

    one_counts = []
    for name, count in dict_of_names_and_counts.items():
        if count < 5:
            one_counts.append(name)

    for item in one_counts:
        del dict_of_names_and_counts[item]
            
    # bar_plotting(dict_of_names_and_counts, title='programming langs and their counts', ylabel='counts of each programming lang')

# -------------------counts of using working fields------------------------
    works = []
    working_field = data["working_field"]

    for raw in working_field:
        for work in raw.split(", "):
            works.append(work)

    works_name = Counter(works).keys()
    works_count = Counter(works).values()

    names_and_counts_of_works = dict(zip(works_name, works_count))

    one_work = []
    for name, count in names_and_counts_of_works.items():
        if count == 1:
            one_work.append(name)

    for item in one_work:
        del names_and_counts_of_works[item]
    

    # bar_plotting(names_and_counts_of_works, title='works and counts of each work', ylabel='counts of each work')

# -------------------works of each ender in each work experience--------------------

    for name in name_and_data(men_work_experience, men, "work_experience", n_d="n"):
        men_works = []
        men_working_experience = men[men["work_experience"] == name]
        for raw in men_working_experience["working_field"]:
            for work in raw.split(", "):
                men_works.append(work)

        men_works_name = Counter(men_works).keys()
        men_works_count = Counter(men_works).values()

        names_and_counts_of_men_works = dict(zip(men_works_name, men_works_count))

        men_one_works = []
        for names, count in names_and_counts_of_men_works.items():
            if count == 1:
                men_one_works.append(names)

        for item in men_one_works:
            del names_and_counts_of_men_works[item]
            
        reshaped_value = ar.reshape(name)
        name = get_display(reshaped_value)

        # bar_plotting(names_and_counts_of_men_works, title='{}' .format(name), ylabel='counts of each work')

    for name in name_and_data(women_work_experience, women, "work_experience", n_d="n"):
        women_works = []
        women_working_experience = women[women["work_experience"] == name]
        for raw in women_working_experience["working_field"]:
            for work in raw.split(", "):
                women_works.append(work)

        women_works_name = Counter(women_works).keys()
        women_works_count = Counter(women_works).values()

        names_and_counts_of_women_works = dict(zip(women_works_name, women_works_count))

        reshaped_value = ar.reshape(name)
        name = get_display(reshaped_value)

        # bar_plotting(names_and_counts_of_women_works, title='{}' .format(name), ylabel='counts of each work')


# -------------------working fields for each salary and work experience-----------------------
    salary = data["salary"]
    for name in name_and_data(salary, data, "salary", n_d="n"):
        data_salary = data[data["salary"] == name]
        data_work_experience = data_salary["work_experience"]
        for name_2 in name_and_data(data_work_experience, data_salary, "work_experience", n_d="n"):
            data_works = []
            working_experience_of_each_salary = data_salary[data_salary["work_experience"] == name_2]
            for raw_2 in working_experience_of_each_salary["working_field"]:
                for work in raw_2.split(", "):
                    data_works.append(work)

            data_works_name = Counter(data_works).keys()    
            data_works_count = Counter(data_works).values()

            names_and_counts_of_works_of_data = dict(zip(data_works_name, data_works_count))

            reshaped_value = ar.reshape(name)
            reshaped_value = ar.reshape(name_2)
            name = get_display(reshaped_value)
            name_2 = get_display(reshaped_value)

            # bar_plotting(names_and_counts_of_works_of_data, title='{} & {}' .format(name, name_2), ylabel=":))))))")    

-------------------programming field for each working field-----------------------
    all_of_working_field = []
    for raw_3 in data["working_field"]:
        for work_2 in raw_3.split(", "):
            all_of_working_field.append(work_2)

    all_of_working_field_name = Counter(all_of_working_field).keys()
    all_of_working_field_count = Counter(all_of_working_field).values()

    name_and_counts_of_working_field = dict(zip(all_of_working_field_name, all_of_working_field_count))

    one_works = []
    for names, count in name_and_counts_of_working_field.items():
        if count == 1:
            one_works.append(names)

    for item in one_works:
        del name_and_counts_of_working_field[item]

    for name_3 in Counter(name_and_counts_of_working_field).keys():
        print(name_3)
        langs_2 = []
        langs_for_learning = []
        for row in data["timestamp"]:
            specific_data_by_timestamp = data[data["timestamp"] == row]
            # print(specific_data_by_timestamp["working_field"])
            if str(name_3) in str(specific_data_by_timestamp["working_field"]):

                programming_lang = specific_data_by_timestamp["programming_lang"]
                programming_lang_for_learning = specific_data_by_timestamp["programming_lang_for_learning"]

                for row_2 in programming_lang:
                    for lang in row_2.split(", "):
                        langs_2.append(lang)

                for row_3 in programming_lang_for_learning:
                    for learning_lang in str(row_3).split(", "):
                        langs_for_learning.append(learning_lang)

        langs_name_2 = Counter(langs_2).keys()
        langs_count_2 = Counter(langs_2).values()

        learning_langs_name = Counter(langs_for_learning).keys()
        learning_langs_count = Counter(langs_for_learning).values()

        ln2 = []
        lfl = []
        for l_n_2 in langs_name_2:
            ln2.append(persian_english(l_n_2))

        for l_f_l in learning_langs_name:
            lfl.append(persian_english(l_f_l))


        dict_of_names_and_counts_of_langs = dict(zip(ln2, langs_count_2))
        dict_of_names_and_counts_of_learning_langs = dict(zip(lfl, learning_langs_count))        

        one_counts = []
        for name, count in dict_of_names_and_counts_of_langs.items():
            if count == 1:
                one_counts.append(name)

        for item in one_counts:
            del dict_of_names_and_counts_of_langs[item]

        one_count_langs = []
        for name, count in dict_of_names_and_counts_of_learning_langs.items():
            if count == 1:
                one_count_langs.append(name)

        for item in one_count_langs:
            del dict_of_names_and_counts_of_learning_langs[item]

        bar_plotting(dict_of_names_and_counts_of_langs, title='programming langs {} use' .format(persian_english(name_3)), ylabel='counts of each programming lang')
        bar_plotting(dict_of_names_and_counts_of_learning_langs, title='programming langs {} like to learn' .format(persian_english(name_3)), ylabel='counts of each programming lang')



# -------------------Andriod Devs salary analisys----------------------
    A = []
    for row_4 in data["timestamp"]:
        specify_data_by_timestamp = data[data["timestamp"] == row_4]
        if specify_data_by_timestamp["work_experience"].all() == "یک تا سه سال":
            if "توسعه دهنده موبایل" in str(specify_data_by_timestamp["working_field"]):
                A.append(specify_data_by_timestamp["salary"].all())
                # if "java" in str(specify_data_by_timestamp["programming_lang"]):

    A_names = Counter(A).keys()
    A_counts = Counter(A).values()

    dict_of_names_and_counts_of_A = dict(zip(persian_writing(A_names), A_counts))
    # bar_plotting(dict_of_names_and_counts_of_A, title='1-3 years of experience in mobile Devs', ylabel='count')
