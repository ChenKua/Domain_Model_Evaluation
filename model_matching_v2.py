# %% [markdown]
# # Set up

import ast
import json
import os
# %%
import pickle
import re
import sys

import networkx as nx
import numpy as np
import openai
import pandas as pd
from openai import OpenAI
from worde4mde import load_embeddings

# %%

# put the huggingface api key
openai_key = "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"
os.environ["OPENAI_API_KEY"] = openai_key

openai.api_key = openai_key

# %%
if len(sys.argv) != 2:
    print("Usage: python script_name.py arg1 arg2")
    sys.exit(1)

g = sys.argv[1]
print("group:", g)


# %%
instructor_dir = "smart_home/"
instructor_input = instructor_dir + "instructor.txt"
student_dir = "smart_home/GX/".replace("GX", g)

student_input = student_dir + "dsl.txt"
student_input
student_out_dir = student_dir + "result/"
student_out_dir

# %%
# First of all, you need to load the embeddings (currently supported: 'sgram-mde' and 'glove-mde')
sgram_mde = load_embeddings("sgram-mde")
glove = load_embeddings("glove-mde")
# sgram_mde["id"]

# %%
# word = 'id'
# sgram_mde.most_similar(positive=[word])


# %%
def inEmbedding(word, embedding):
    try:
        return True, embedding[word]
    except:
        return False, None


# %%


def splitCamelCase(word):
    splitted = re.sub("([A-Z][a-z]+)", r" \1", re.sub("([A-Z]+)", r" \1", word)).split()
    return splitted


splitCamelCase("device ID")

# %%
client = OpenAI()


def run_llm(prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content


# %%

client = OpenAI()


def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding


# %%
def get_all_info(class_index, class_nodes, list_of_classes, list_edges, need_edge=True):
    result = ""
    result += list_of_classes[class_index] + "\n"
    node = class_nodes[class_index]
    if "abstract" in node:
        node = node.replace("abstract", "").strip()
    if "Abstract" in node:
        node = node.replace("Abstract", "").strip()
    if need_edge:
        for edge in list_edges:
            element = [i.strip() for i in edge.split()]
            if node in element:
                result += edge + "\n"

    return result


# %%
def map_classes(raw_1, raw_2, dict_attr, thresh=0.45):
    # raw_1: nodes from reference solution
    # raw_2: nodes from student solution
    # dict_attr: dictionary for embeddings
    # thresh for subst cost
    # map class lists raw_1 and raw_2
    def node_subst_cost_attr(node1, node2):
        # threshod as 0.45
        if dict_attr[node1["name"]][node2["name"]] < thresh:
            return 3
        else:
            return 1 - dict_attr[node1["name"]][node2["name"]]

    G_att_1 = nx.Graph()
    G_att_2 = nx.Graph()
    for node in raw_1:
        G_att_1.add_node(node, name=node)

    for node in raw_2:
        G_att_2.add_node(node, name=node)

    for v in nx.optimize_edit_paths(
        G_att_1,
        G_att_2,
        node_subst_cost=node_subst_cost_attr,
        edge_match=None,
        timeout=20,
    ):
        minv = v
    # minv

    return minv


# %% [markdown]
# # Group


# %%
class Grader:
    def __init__(self):
        self.ref = None
        self.stu = None


# %%
grader = Grader()

# %% [markdown]
# ## Class

# %% [markdown]
# ### Define metadata


# %%
class ClassInfo:
    def __init(self):
        self.cls_atr = {}
        self.cls_name = []
        self.raw_dsl = []
        self.rel = []


# %%
ref_cls = ClassInfo()
stu_cls = ClassInfo()

# %%
grader.ref = ref_cls
grader.stu = stu_cls

# %%
with open(instructor_input, "r") as file:
    # Read the entire content of the file
    instructor_all = file.read()

with open(student_input, "r") as file:
    # Read the entire content of the file
    student_all = file.read()

# %%
shas_sol = instructor_all.split("Relationships:")[0]
stu_sol_g = student_all.split("Relationships:")[0]  # student solution

# %%
ref_classes_raw = []
tmp = shas_sol.strip().splitlines()
ref_classes_raw = [i.strip() for i in tmp if len(i) > 0]
ref_classes_raw

reference_class = []
tmp = shas_sol.strip().splitlines()
reference_class = [i.split("(")[0].strip() for i in tmp if len(i) > 0]

# %%
stu_classes_raw = []
tmp = stu_sol_g.strip().splitlines()
stu_classes_raw = [i.strip() for i in tmp if len(i) > 0]
stu_classes_raw

tmp = stu_sol_g.strip().splitlines()
stu_class = [i.split("(")[0].strip() for i in tmp if len(i) > 0]
stu_class

# %%
ref_attributes = {}
enum_index = ref_classes_raw.index("Enumerations:")
regular_index = ref_classes_raw.index("Classes:")
for cla, dsl in zip(reference_class, ref_classes_raw):
    if dsl == "Enumerations:" or dsl == "Classes:":
        continue
    else:
        index = ref_classes_raw.index(dsl)
        if index > regular_index:
            class_type = "regular"
            if "abstract" in dsl:
                class_type = "abstract"
        else:
            class_type = "enum"
        ref_attributes[cla] = {
            "score": 0,
            "type": class_type,
            "dsl": dsl,
            "counterpart": None,
            "attributes": {},
        }

        attributes = dsl.split("(")[1][:-1].split(",")
        for attr in attributes:
            attr = attr.strip()
            if len(attr) > 0:
                ref_attributes[cla]["attributes"][attr] = {
                    "score": 0,
                    "counterpart": None,
                }

# %%
reference_class.remove("Enumerations:")
reference_class.remove("Classes:")

ref_classes_raw.remove("Enumerations:")
ref_classes_raw.remove("Classes:")

# %%
ref_cls.cls_name = reference_class
ref_cls.raw_dsl = ref_classes_raw
ref_cls.cls_atr = ref_attributes

# %%
stu_attributes = {}
enum_index = stu_classes_raw.index("Enumerations:")
regular_index = stu_classes_raw.index("Classes:")

for cla, dsl in zip(stu_class, stu_classes_raw):
    if dsl == "Enumerations:" or dsl == "Classes:":
        continue
    else:
        index = stu_classes_raw.index(dsl)
        if index > regular_index:
            class_type = "regular"
            if "abstract" in dsl:
                class_type = "abstract"
        else:
            class_type = "enum"

        stu_attributes[cla] = {
            "score": 0,
            "type": class_type,
            "dsl": dsl,
            "counterpart": None,
            "attributes": {},
        }

        print(dsl)
        attributes = dsl.split("(")[1][:-1].split(",")
        for attr in attributes:
            attr = attr.strip()
            if len(attr) > 0:
                stu_attributes[cla]["attributes"][attr] = {
                    "score": 0,
                    "counterpart": None,
                }

# %%
stu_class.remove("Enumerations:")
stu_class.remove("Classes:")

stu_classes_raw.remove("Enumerations:")
stu_classes_raw.remove("Classes:")

# %%
stu_cls.cls_name = stu_class
stu_cls.raw_dsl = stu_classes_raw
stu_cls.cls_atr = stu_attributes

# %% [markdown]
# ## Edges

# %% [markdown]
# ### reference and student solutions

# %%
shas_edges = instructor_all.split("Relationships:")[1]
shas_G2_edges = student_all.split("Relationships:")[1]  # student solution

# %%
shas_edges

# %%
shas_edges

# %%
shas_edges = shas_edges.replace("0..*", "*")

# %%
shas_G2_edges = shas_G2_edges.replace("0..*", "*")

# %%
tmp = shas_edges.strip().splitlines()
ref_edges = [i.strip() for i in tmp if len(i) > 0]

for i in ref_edges:
    length = len(i.split())
    if length == 5 or length == 3:
        pass
    else:
        print("Reference Length error:", i)

tmp = shas_G2_edges.strip().splitlines()
stu_edges = [i.strip() for i in tmp if len(i) > 0]

for i in stu_edges:
    length = len(i.split())
    if length == 5 or length == 3:
        pass
    else:
        print("Student Length error:", i)


# %%
class Relationship:
    def __init__(self):
        self.rels = []  # list of dict{}
        self.raw_dsl = []

    # find first non-matched or matched reltionshipi given dsl
    def find_relation(self, dsl, matched=False):
        for index, i in enumerate(self.rels):
            if i["dsl"] == dsl and i["counterpart"] is None:
                return index, i

        return None


# %%
ref_edges_obj = Relationship()
stu_edges_obj = Relationship()


ref_edges_dict = []
for e in ref_edges:
    ref_edges_dict.append({"dsl": e, "score": 0, "counterpart": None})

ref_edges_obj.rels = ref_edges_dict
ref_edges_obj.raw_dsl = ref_edges

stu_edges_dict = []
for e in stu_edges:
    stu_edges_dict.append({"dsl": e, "score": 0, "counterpart": None})

stu_edges_obj.rels = stu_edges_dict
stu_edges_obj.raw_dsl = stu_edges

# %%
# link to classInfo object
ref_cls.rel = ref_edges_obj
stu_cls.rel = stu_edges_obj

# %%
edges = [ref_edges_obj, stu_edges_obj]

# %% [markdown]
# ## Getting embedding


# %%
def get_mde_embedding(text, embedding):
    # >>> get_mde_embedding("WhatDevice", sgram_mde)
    words = splitCamelCase(text)
    lowercase_list = [s.lower() for s in words]
    counter = 0
    emb = np.zeros(300)
    for w in lowercase_list:
        try:
            emb += embedding[w]
            counter += 1
        except:
            # if failed in emb the complete word, embed the token
            tmp = np.zeros(300)
            for char in list(w):
                tmp += embedding[char]
            emb += tmp / len(w)
            counter += 1
    return emb / counter


# %%
def cosine_distance(emb_i, emb_j):
    return np.dot(emb_i, emb_j) / (np.linalg.norm(emb_i) * np.linalg.norm(emb_j))


# %%
# # all info
# similarity_all_g2 = []
# similarity_mde = []

# mde_embedding = sgram_mde

# for index, node in enumerate(reference_class):

#   text_1 = get_all_info(index, reference_class, ref_classes_raw, ref_edges, False)

#   emb_i = get_embedding(text_1)

#   cls = node.split()[-1].strip() # get the class name, remove abstract key word
#   mde_emb_i = get_mde_embedding(cls, mde_embedding)

#   pair = []
#   mde_pair = []
#   for j, stu_node in enumerate(stu_class):

#     text_2 = get_all_info(j, stu_class, stu_classes_raw, stu_edges, False)
#     emb_j = get_embedding(text_2)
#     sim = cosine_distance(emb_i, emb_j)

#     cls = stu_node.split()[-1].strip() # get the class name, remove abstract key word
#     mde_emb_j = get_mde_embedding(cls, mde_embedding)

#     mde_sim = cosine_distance(mde_emb_i, mde_emb_j)

#     pair.append(sim)
#     mde_pair.append(mde_sim)

#   # apply third quartile
#   similarity_all_g2.append(pair)
#   similarity_mde.append(mde_pair)


# %%

# similarity_all_g2_np = np.array(similarity_all_g2)
# similarity_mde_np = np.array(similarity_mde)

# similarity_all_np = 1 * similarity_all_g2_np + 0.0 * similarity_mde_np

# %%
# row_percentiles = np.percentile(similarity_all_np,90, axis=1)
# row_percentiles = row_percentiles[:, np.newaxis]
# row_percentiles = np.repeat(row_percentiles, 24, axis = 1)

# %%
# similarity_all_np = np.where(similarity_all_np < row_percentiles,
#                              -2,
#                              similarity_all_np)

# %%
# import pandas as pd

# df = pd.DataFrame(index=reference_class, columns=stu_class, data=similarity_all_np)
# df

# %%
# dict_sim_all_g2 = {}

# for i in range(len(reference_class)):
#   dict_sim_all_g2[reference_class[i]] = {}
#   for j in range(len(stu_class)):
#     dict_sim_all_g2[reference_class[i]][stu_class[j]] = similarity_all_np[i][j]


# %% [markdown]
# ## Stage 1.1 Class name mapping

# %%
# get name embedding
# all info
similarity_mde = []
mde_embedding = sgram_mde
threshold = 0.7

for index, node in enumerate(ref_cls.cls_name):
    cls = node.split()[-1].strip()  # get the class name, remove abstract key word
    mde_emb_i = get_mde_embedding(cls, mde_embedding)
    pair = []
    mde_pair = []
    for j, stu_node in enumerate(stu_cls.cls_name):
        cls = stu_node.split()[
            -1
        ].strip()  # get the class name, remove abstract key word
        mde_emb_j = get_mde_embedding(cls, mde_embedding)
        mde_sim = cosine_distance(mde_emb_i, mde_emb_j)
        mde_pair.append(mde_sim)

    # apply third quartile
    similarity_mde.append(mde_pair)

dict_sim_word = {}
for i in range(len(ref_cls.cls_name)):
    dict_sim_word[ref_cls.cls_name[i]] = {}
    for j in range(len(stu_cls.cls_name)):
        dict_sim_word[ref_cls.cls_name[i]][stu_cls.cls_name[j]] = similarity_mde[i][j]

# %%
# import pandas as pd

# df = pd.DataFrame(index=reference_class, columns=stu_class, data=similarity_mde)
# df

# %% [markdown]
# ### Stage 1.1.1 Mapping (enum / regular + abstract)

# %%
ref_enum = []
ref_reg_cls = []
stu_enum = []
stu_reg_cls = []

for enum in ref_cls.cls_name:
    if ref_cls.cls_atr[enum]["type"] == "enum":
        ref_enum.append(enum)
    else:
        ref_reg_cls.append(enum)

for enum in stu_cls.cls_name:
    if stu_cls.cls_atr[enum]["type"] == "enum":
        stu_enum.append(enum)
    else:
        stu_reg_cls.append(enum)

# %%
enum_mapping = map_classes(ref_enum, stu_enum, dict_sim_word, thresh=0.5)
enum_mapping[0]

# %%
cls_mapping = map_classes(ref_reg_cls, stu_reg_cls, dict_sim_word, thresh=0.5)
cls_mapping[0]

# %%
mapping = enum_mapping[0] + cls_mapping[0]

for map in mapping:
    if map[0] and map[1]:
        ref_cls.cls_atr[map[0]]["score"] = 1
        ref_cls.cls_atr[map[0]]["counterpart"] = map[1]

        stu_cls.cls_atr[map[1]]["score"] = 1
        stu_cls.cls_atr[map[1]]["counterpart"] = map[0]

        if ref_cls.cls_atr[map[0]]["type"] != stu_cls.cls_atr[map[1]]["type"]:
            # type mismatch
            ref_cls.cls_atr[map[0]]["score"] = 0.5
            stu_cls.cls_atr[map[1]]["score"] = 0.5

# %%
ref_cls.cls_atr

# %% [markdown]
# ## Stage 1.2 Class Mapping (with all info)

# %%
ref_classes = []
stu_classes = []

for cls in ref_cls.cls_name:
    if ref_cls.cls_atr[cls]["counterpart"] == None:
        ref_classes.append(cls)

for cls in stu_cls.cls_name:
    if stu_cls.cls_atr[cls]["counterpart"] == None:
        stu_classes.append(cls)

# %%
# get name embedding
# all info
similarity_all = []
mde_embedding = sgram_mde
threshold = 0.7

for index, node in enumerate(ref_cls.cls_name):
    text_1 = get_all_info(
        index, ref_cls.cls_name, ref_cls.raw_dsl, ref_cls.rel.raw_dsl, True
    )
    emb_i = get_embedding(text_1)
    mde_pair = []
    for j, stu_node in enumerate(stu_cls.cls_name):
        text_2 = get_all_info(
            j, stu_cls.cls_name, stu_cls.raw_dsl, stu_cls.rel.raw_dsl, True
        )
        emb_j = get_embedding(text_2)
        mde_sim = cosine_distance(emb_i, emb_j)
        mde_pair.append(mde_sim)

    # apply third quartile
    similarity_all.append(mde_pair)

dict_sim_all = {}
for i in range(len(ref_cls.cls_name)):
    dict_sim_all[ref_cls.cls_name[i]] = {}
    for j in range(len(stu_cls.cls_name)):
        dict_sim_all[ref_cls.cls_name[i]][stu_cls.cls_name[j]] = similarity_all[i][j]

# %%
mapping = map_classes(ref_classes, stu_classes, dict_sim_all, 0.8)
mapping[0]

# %%
for map in mapping[0]:
    if map[0] and map[1]:
        ref_cls.cls_atr[map[0]]["score"] = 1
        ref_cls.cls_atr[map[0]]["counterpart"] = map[1]

        stu_cls.cls_atr[map[1]]["score"] = 1
        stu_cls.cls_atr[map[1]]["counterpart"] = map[0]

        if ref_cls.cls_atr[map[0]]["type"] != stu_cls.cls_atr[map[1]]["type"]:
            # type mismatch
            ref_cls.cls_atr[map[0]]["score"] = 0.5
            stu_cls.cls_atr[map[1]]["score"] = 0.5

# %%
dict_sim_all["BinaryOp"]

# %% [markdown]
# ## Stage 2.1 Attribute mapping


# %%
def get_cosine_disntance(text1, text2, embedding):
    avg = np.sum(embedding[text1], axis=0)
    emb_i = avg / len(text1)

    avg = np.sum(embedding[text2], axis=0)
    emb_j = avg / len(text2)

    return np.dot(emb_i, emb_j) / (np.linalg.norm(emb_i) * np.linalg.norm(emb_j))


# %%
def create_cosine_distance_dict(attr_1, attr_2, embedding):
    # attr_1: list[list] split camel case into separated case
    # attr_2: list[list] split camel case into separated case
    # embedding:
    # raw_1: list[str] camcel case attributes
    # raw_2: list[str] camcel case attributes

    # create cosine distance between two attributes with embeeding

    # >>> dic = createCosineDistance(['deviceStatus', 'deviceId'], ['id'], sgram_mde)
    similarities = []
    for att in attr_1:
        emb_i = get_mde_embedding(att, embedding)
        pair = []
        for attribute in attr_2:
            emb_j = get_mde_embedding(attribute, embedding)

            sim = np.dot(emb_i, emb_j) / (np.linalg.norm(emb_i) * np.linalg.norm(emb_j))
            pair.append(sim)

        similarities.append(pair)

    dict_attr = {}
    for i in range(len(attr_1)):
        dict_attr[attr_1[i]] = {}
        for j in range(len(attr_2)):
            dict_attr[attr_1[i]][attr_2[j]] = similarities[i][j]

    return dict_attr


# %%
def map_attributes(raw_1, raw_2, dict_attr, threshold=0.5):
    # map attributes lists raw_1 and raw_2
    # >>> mapAttributes(['deviceStatus'], ['id'], dic)[0]
    def node_subst_cost_attr(node1, node2):
        # threshod as 0.45
        if dict_attr[node1["name"]][node2["name"]] < threshold:
            return 3
        else:
            return 1 - dict_attr[node1["name"]][node2["name"]]

    G_att_1 = nx.Graph()
    G_att_2 = nx.Graph()
    for node in raw_1:
        G_att_1.add_node(node, name=node)

    for node in raw_2:
        G_att_2.add_node(node, name=node)

    for v in nx.optimize_edit_paths(
        G_att_1,
        G_att_2,
        node_subst_cost=node_subst_cost_attr,
        edge_match=None,
        timeout=20,
    ):
        minv = v
    # minv

    return minv


# %%
def check_attributes_type(attr_1, attr_2, ref_dict, stu_dict):
    # given two attribute, compare whether their type can match
    attr_1 = attr_1.split()  # from reference solution do not need to check it
    attr_2 = attr_2.split()

    # if enumerate literal and attributes
    # if len(attr_1) != len(attr_2):
    #   return 0.5, 0.5

    # if an attributes use a regular class as its type
    if len(attr_2) == 2:
        t = attr_2[0].strip()
        cls = stu_dict.get(t, None)
        if cls is not None and (
            stu_dict[t]["type"] == "regular" or stu_dict[t]["type"] == "abstract"
        ):
            return 0.5, 0.5

    return 1, 1


# %% [markdown]
# ### Stage 2.1.1 Attribute <-> Attribute (mapped classes)

# %%
# map classes
pairs = []

# get matched pairs
for key in ref_cls.cls_atr:
    if ref_cls.cls_atr[key]["counterpart"] != None:
        pair = [key, ref_cls.cls_atr[key]["counterpart"]]
        pairs.append(pair)

for pair in pairs:
    if pair[0] and pair[1]:
        print(pair)

        # map attributes:
        # matched_ref = set()
        # matched_attr = set()

        raw_1 = []
        for attributes in ref_cls.cls_atr[pair[0]]["attributes"]:
            raw_1.append(attributes)

        raw_2 = []
        for attributes in stu_cls.cls_atr[pair[1]]["attributes"]:
            raw_2.append(attributes)

        cos_dict = create_cosine_distance_dict(raw_1, raw_2, sgram_mde)
        mappings = map_attributes(raw_1, raw_2, cos_dict)[0]
        print("mapping", mappings)

        for mapping in mappings:
            if mapping[0] != None and mapping[1] != None:
                scores = check_attributes_type(
                    mapping[0], mapping[1], ref_cls.cls_atr, stu_cls.cls_atr
                )
                ref_cls.cls_atr[pair[0]]["attributes"][mapping[0]]["score"] = scores[0]
                ref_cls.cls_atr[pair[0]]["attributes"][mapping[0]]["counterpart"] = (
                    mapping[1],
                    pair[1],
                )
                stu_cls.cls_atr[pair[1]]["attributes"][mapping[1]]["score"] = scores[1]
                stu_cls.cls_atr[pair[1]]["attributes"][mapping[1]]["counterpart"] = (
                    mapping[0],
                    pair[0],
                )

        print("=" * 20)

# %% [markdown]
# ### Stage 2.1.2 Attribute <-> Attribute (between any classes)


# %%
def create_cosine_distance_list(attr_1, attr_2, embedding):
    # attr_1: list[list] split camel case into separated case
    # attr_2: list[list] split camel case into separated case
    # embedding:
    # raw_1: list[str] camcel case attributes
    # raw_2: list[str] camcel case attributes

    # create cosine distance between two attributes with embeeding

    # >>> dic = createCosineDistance(['deviceStatus', 'deviceId'], ['id'], sgram_mde)
    similarities = []
    for att in attr_1:
        emb_i = get_mde_embedding(att, embedding)
        pair = []
        for attribute in attr_2:
            emb_j = get_mde_embedding(attribute, embedding)

            sim = np.dot(emb_i, emb_j) / (np.linalg.norm(emb_i) * np.linalg.norm(emb_j))
            pair.append(sim)

        similarities.append(pair)

    return similarities


# %%
def combine_two_dict(
    list_1, list_2, atr_1, atr_2, cls_1, cls_2, weight_1=0.9, weight_2=0.1
):
    # list_1: similarity between cls
    # list_2: cos similarity between attributes
    if weight_1 + weight_2 != 1:
        raise ValueError("weight_1 + weight_2 != 1")
    result = {}
    for i in range(len(atr_1)):
        atr_r = atr_1[i]
        cls_r = cls_1[i]
        tmp_ref = (atr_r, cls_r)
        result[tmp_ref] = {}
        for j in range(len(atr_2)):
            atr_s = atr_2[j]
            cls_s = cls_2[j]
            tmp_stu = (atr_s, cls_s)

            result[tmp_ref][tmp_stu] = weight_1 * list_1[i][j] + weight_2 * list_2[i][j]

    return result


# %%
# attr between any classes

raw_1 = []
ref_source = []
tup_r = []
# get attributes on instrucotr sides
for cls in ref_cls.cls_atr:
    for attributes in ref_cls.cls_atr[cls]["attributes"]:
        if ref_cls.cls_atr[cls]["attributes"][attributes]["counterpart"] == None:
            raw_1.append(attributes)
            ref_source.append(cls)
            tup_r.append((attributes, cls))

raw_2 = []
stu_source = []
tup_s = []
# get attributes on student sides
for cls in stu_cls.cls_atr:
    for attributes in stu_cls.cls_atr[cls]["attributes"]:
        if stu_cls.cls_atr[cls]["attributes"][attributes]["counterpart"] == None:
            raw_2.append(attributes)
            stu_source.append(cls)
            tup_s.append((attributes, cls))

list_1 = create_cosine_distance_list(raw_1, raw_2, sgram_mde)
list_2 = create_cosine_distance_list(ref_source, stu_source, sgram_mde)
combined = combine_two_dict(list_1, list_2, raw_1, raw_2, ref_source, stu_source)

mappings = map_attributes(tup_r, tup_s, combined)[0]

for mapping in mappings:
    print(mapping)
    if mapping[0] != None and mapping[1] != None:
        scores = check_attributes_type(
            mapping[0][0], mapping[1][0], ref_cls.cls_atr, stu_cls.cls_atr
        )
        ref_cls.cls_atr[mapping[0][1]]["attributes"][mapping[0][0]]["score"] = min(
            scores[0], 0.5
        )
        ref_cls.cls_atr[mapping[0][1]]["attributes"][mapping[0][0]][
            "counterpart"
        ] = mapping[1]

        stu_cls.cls_atr[mapping[1][1]]["attributes"][mapping[1][0]]["score"] = min(
            scores[1], 0.5
        )
        stu_cls.cls_atr[mapping[1][1]]["attributes"][mapping[1][0]][
            "counterpart"
        ] = mapping[0]

print("=" * 20)

# %%
stu_cls.cls_atr["SmartHome"]

# %%
ref_cls.cls_atr["Address"]

# %% [markdown]
# ## Stage 2.2.1 Attribute mapping atr -> cls

# %%
#  get non-mapped attributes on instrucotr side

raw_1 = []
ref_source = []
tup_r = []
# get attributes on instrucotr sides
for cls in ref_cls.cls_atr:
    for attributes in ref_cls.cls_atr[cls]["attributes"]:
        if ref_cls.cls_atr[cls]["attributes"][attributes]["counterpart"] == None:
            raw_1.append(attributes)
            ref_source.append(cls)
            tup_r.append((attributes, cls))

raw_2 = []
stu_source = []
tup_s = []
# get un-mapped class on student sides
for cls in stu_cls.cls_atr:
    if stu_cls.cls_atr[cls]["counterpart"] == None:
        raw_2.append(cls)
        stu_source.append(cls)
        tup_s.append((cls, cls))

list_1 = create_cosine_distance_list(raw_1, raw_2, sgram_mde)
list_2 = create_cosine_distance_list(ref_source, stu_source, sgram_mde)
combined = combine_two_dict(list_1, list_2, raw_1, raw_2, ref_source, stu_source)

mappings = map_attributes(tup_r, tup_s, combined)[0]

for mapping in mappings:
    print(mapping)
    if mapping[0] != None and mapping[1] != None:
        # scores = check_attributes_type(mapping[0][0], mapping[1][0], ref_cls.cls_atr, stu_cls.cls_atr)
        ref_cls.cls_atr[mapping[0][1]]["attributes"][mapping[0][0]]["score"] = 0.5
        ref_cls.cls_atr[mapping[0][1]]["attributes"][mapping[0][0]]["counterpart"] = (
            None,
            mapping[1][1],
        )

        stu_cls.cls_atr[mapping[1][1]]["score"] = 0.5
        stu_cls.cls_atr[mapping[1][1]]["counterpart"] = mapping[0]

print("=" * 20)


# %% [markdown]
# ## Stage 2.2.2 Attribute mapping cls -> atr

# %%
#  get non-mapped cls on instrucotr side

raw_1 = []
ref_source = []
tup_r = []
# get class on instrucotr sides
for cls in ref_cls.cls_atr:
    if ref_cls.cls_atr[cls]["counterpart"] == None:
        raw_1.append(cls)
        ref_source.append(cls)
        tup_r.append((cls, cls))

raw_2 = []
stu_source = []
tup_s = []
# get un-mapped class on student sides
for cls in stu_cls.cls_atr:
    for attributes in stu_cls.cls_atr[cls]["attributes"]:
        if stu_cls.cls_atr[cls]["attributes"][attributes]["counterpart"] == None:
            raw_2.append(attributes)
            stu_source.append(cls)
            tup_s.append((attributes, cls))

list_1 = create_cosine_distance_list(raw_1, raw_2, sgram_mde)
list_2 = create_cosine_distance_list(ref_source, stu_source, sgram_mde)
combined = combine_two_dict(list_1, list_2, raw_1, raw_2, ref_source, stu_source)

mappings = map_attributes(tup_r, tup_s, combined)[0]

for mapping in mappings:
    print(mapping)
    if mapping[0] != None and mapping[1] != None:
        # scores = check_attributes_type(mapping[0][0], mapping[1][0], ref_cls.cls_atr, stu_cls.cls_atr)
        ref_cls.cls_atr[mapping[0][1]]["attributes"][mapping[0][0]]["score"] = 0.5
        ref_cls.cls_atr[mapping[0][1]]["attributes"][mapping[0][0]][
            "counterpart"
        ] = mapping[1]

        stu_cls.cls_atr[mapping[1][1]]["score"] = 0.5
        stu_cls.cls_atr[mapping[1][1]]["counterpart"] = (None, mapping[0][1])

print("=" * 20)


# %% [markdown]
# ## Stage 3: Relationship mapping


# %%
def check_relations_classes(ref_index, stu_index, ref_elements, stu_elements):
    # ref_index: index of the element in the dsl
    # stu_index: index of the element in the dsl
    # ref_elements: list[str] elements in the dsl
    # stu_elements: list[str] elements in the dsl

    ref_class_1 = ref_elements[ref_index]
    # check whether this is an abstract class
    dict_keys = list(ref_attributes.keys())
    if not ref_class_1 in dict_keys:
        abstract = "abstract " + ref_class_1
        ref_class_1 = abstract

    true_pair = ref_attributes[ref_class_1]["counterpart"]
    if true_pair == None:
        boolean_1 = False
    else:
        tmp = true_pair.replace("abstract ", "")
        boolean_1 = stu_elements[stu_index] == tmp
    return boolean_1


# %% [markdown]
# #### Compare rel

# %%


def compare_edges(ref_e, stu_e):
    # compare if two relationships match
    # return bool, score, score

    ref_elements = ref_e.split()
    stu_elements = stu_e.split()
    # print(ref_elements, stu_elements)

    # exact match first
    # length must match
    n_ref = len(ref_elements)
    n_stu = len(stu_elements)
    if n_ref == n_stu and n_ref == 5:
        # all element must match
        boolean_1 = check_relations_classes(1, 1, ref_elements, stu_elements)

        boolean_4 = check_relations_classes(4, 4, ref_elements, stu_elements)

        # type
        boolean_2 = ref_elements[2] == stu_elements[2]

        # association
        boolean_0 = ref_elements[0] == stu_elements[0]

        # association
        boolean_3 = ref_elements[3] == stu_elements[3]

        if boolean_0 and boolean_1 and boolean_2 and boolean_3 and boolean_4:
            print("exact match success")
            print(ref_e, "|||", stu_e)
            return True, 1, 1

        boolean_1_4 = False
        boolean_4_1 = False
        boolean_1_4 = check_relations_classes(1, 4, ref_elements, stu_elements)
        boolean_4_1 = check_relations_classes(4, 1, ref_elements, stu_elements)

        # check if the relationship is fliped, this only works for associate, not containment
        if "associate" in ref_elements[2] and "associate" in stu_elements[2]:
            # association
            boolean_0 = ref_elements[0] == stu_elements[3]

            # association
            boolean_3 = ref_elements[3] == stu_elements[0]
            # boolean_1_4 = check_relations_classes(1,4,ref_elements,stu_elements )
            # boolean_4_1 = check_relations_classes(4,1,ref_elements,stu_elements )

        if boolean_0 and boolean_1_4 and boolean_3 and boolean_4_1:
            print("match success, flipped associate")
            print(ref_e, "|||", stu_e)
            # ref_dict[ref_e]["score"] = 1
            # ref_dict[ref_e]["counterpart"] = stu_e

            # stu_dict[stu_e]["score"] = 1
            # stu_dict[stu_e]["counterpart"] = ref_e
            return True, 1, 1

        # check if relationship is partially match
        if (boolean_1 and boolean_4) or (boolean_1_4 and boolean_4_1):
            print("match partially success")
            print(ref_e, "|||", stu_e)
            # ref_dict[ref_e]["score"] = 0.5
            # ref_dict[ref_e]["counterpart"] = stu_e

            # stu_dict[stu_e]["score"] = 0.5
            # stu_dict[stu_e]["counterpart"] = ref_e
            return True, 0.5, 0.5

    if n_ref == n_stu and n_ref == 3:
        # all element must match
        boolean_0 = check_relations_classes(0, 0, ref_elements, stu_elements)
        boolean_2 = check_relations_classes(2, 2, ref_elements, stu_elements)

        # type
        boolean_1 = ref_elements[1] == stu_elements[1]

        if boolean_0 and boolean_1 and boolean_2:
            print("match success")
            print(ref_e, "|||", stu_e)
            # ref_dict[ref_e]["score"] = 1
            # ref_dict[ref_e]["counterpart"] = stu_e

            # stu_dict[stu_e]["score"] = 1
            # stu_dict[stu_e]["counterpart"] = ref_e
            return True, 1, 1

    return False, 0, 0


# %%
compare_edges(
    "BinaryExpression inherit BooleanExpression", "* ControlCommand associate * Action"
)

# %%
matched_stu_edges = set()

for i, ref_tmp in enumerate(edges[0].raw_dsl):
    for j, stu_tmp in enumerate(edges[1].raw_dsl):
        if not j in matched_stu_edges:
            result = compare_edges(ref_tmp, stu_tmp)
            if result[0]:
                matched_stu_edges.add(j)
                edges[0].rels[i]["score"] = result[1]
                edges[0].rels[i]["counterpart"] = stu_tmp

                edges[1].rels[j]["score"] = result[2]
                edges[1].rels[j]["counterpart"] = ref_tmp

# %%
# ref_edges_obj.rels

# %% [markdown]
# ## Result: Precision/Recall/F1

# %% [markdown]
# ### save matching to disk

# %%

if not os.path.exists(student_out_dir):
    os.makedirs(student_out_dir)

# %%
with open(student_out_dir + "matching.pkl", "wb") as outp:
    pickle.dump(grader, outp, pickle.HIGHEST_PROTOCOL)

# %%


# as requested in comment

with open(student_out_dir + "solution_matching.txt", "w") as file:
    file.write(json.dumps(grader.ref.cls_atr))


with open(student_out_dir + "student_matching.txt", "w") as file:
    file.write(json.dumps(grader.stu.cls_atr))

with open(student_out_dir + "solution_matching_relationship.txt", "w") as file:
    file.write(json.dumps(grader.ref.rel.rels))


with open(student_out_dir + "student_matching_relationship.txt", "w") as file:
    file.write(json.dumps(grader.stu.rel.rels))

# %%


# # as requested in comment

# with open(student_dir + "human_eval/" + 'ref_meta_cls.py', 'w') as file:
#      file.write(json.dumps(grader.ref.cls_atr))


# with open(student_dir + "human_eval/" + 'stu_meta_cls.py', 'w') as file:
#      file.write(json.dumps(grader.stu.cls_atr))

# with open(student_dir + "human_eval/" + 'ref_meta_rels.py', 'w') as file:
#      file.write(json.dumps(grader.ref.rel.rels))


# with open(student_dir + "human_eval/" + 'stu_meta_rels.py', 'w') as file:
#      file.write(json.dumps(grader.stu.rel.rels))

# %%
algo_result = {}
algo_result["class"] = {"precision": 0, "recall": 0, "f1": 0}
algo_result["attribute"] = {"precision": 0, "recall": 0, "f1": 0}
algo_result["relationship"] = {"precision": 0, "recall": 0, "f1": 0}

# %% [markdown]
# ### Class

# %%
# recell
count = 0
recall = 0
for key in list(ref_attributes.keys()):
    count += 1
    recall += ref_attributes[key]["score"]
print(count, recall)

algo_result["class"]["recall"] = recall / count

# %%
# precision
count = 0
precision = 0
for key in list(stu_attributes.keys()):
    count += 1
    precision += stu_attributes[key]["score"]

print(count, precision)

algo_result["class"]["precision"] = precision / count
algo_result["class"]["f1"] = (
    2
    * (algo_result["class"]["recall"] * algo_result["class"]["precision"])
    / (algo_result["class"]["recall"] + algo_result["class"]["precision"])
)


# %% [markdown]
# ### Attribute

# %%
# recall
count = 0
recall = 0
for key in list(ref_attributes.keys()):
    attrs = ref_attributes[key]["attributes"]

    for att in attrs:
        count += 1
        recall += ref_attributes[key]["attributes"][att]["score"]
print(count, recall)

algo_result["attribute"]["recall"] = recall / count

# %%
count = 0
precision = 0
for key in list(stu_attributes.keys()):
    attrs = stu_attributes[key]["attributes"]

    for att in attrs:
        count += 1
        precision += stu_attributes[key]["attributes"][att]["score"]
print(count, precision)

algo_result["attribute"]["precision"] = precision / count

r = algo_result["attribute"]["recall"]
p = algo_result["attribute"]["precision"]

algo_result["attribute"]["f1"] = 2 * (r * p) / (r + p)


# %% [markdown]
# ### Relationship

# %%
count = 0
recall = 0
for tmp in edges[0].rels:
    attrs = tmp["score"]

    count += 1
    recall += attrs
print(count, recall)

algo_result["relationship"]["recall"] = recall / count

# %%
count = 0
precision = 0
for tmp in edges[1].rels:
    attrs = tmp["score"]

    count += 1
    precision += attrs
print(count, precision)

algo_result["relationship"]["precision"] = precision / count
r = algo_result["relationship"]["recall"]
p = algo_result["relationship"]["precision"]
algo_result["relationship"]["f1"] = 2 * (r * p) / (r + p)


# %%

# as requested in comment

with open(student_out_dir + "algo_result.txt", "w") as file:
    file.write(json.dumps(algo_result))

# %% [markdown]
# ## Comparing with manual evaluation

# %%


class HumanEvaluation(object):
    def __init__(self, ref_cls=None, stu_cls=None, ref_rels=None, stu_rels=None):
        self.ref_cls = ref_cls
        self.stu_cls = stu_cls
        self.ref_rels = ref_rels
        self.stu_rels = stu_rels


group = HumanEvaluation()


# %%


# as requested in comment

with open(student_dir + "human_eval/" + "ref_meta_cls.py", "r") as file:
    content = file.read()
    ref_cls_human = ast.literal_eval(content)
    group.ref_cls = ref_cls_human

with open(student_dir + "human_eval/" + "stu_meta_cls.py", "r") as file:
    content = file.read()
    stu_cls_human = ast.literal_eval(content)
    group.stu_cls = stu_cls_human

with open(student_dir + "human_eval/" + "ref_meta_rels.py", "r") as file:
    content = file.read()
    ref_rel_human = ast.literal_eval(content)
    group.ref_rels = ref_rel_human

with open(student_dir + "human_eval/" + "stu_meta_rels.py", "r") as file:
    content = file.read()
    stu_rel_human = ast.literal_eval(content)
    group.stu_rels = stu_rel_human

# %% [markdown]
# ### class

# %%
# # human matching
# ref_cls_human = {'DeviceStatus': {'score': 1,
#   'counterpart': 'DeviceStatus',
#   'attributes': {'Activated': {'score': 1,
#     'counterpart': ('Activated', 'DeviceStatus')},
#    'Deactivated': {'score': 1,
#     'counterpart': ('Deactivated', 'DeviceStatus')}}},
#                  # checked above
#  'CommandType': {'score': 1,
#   'counterpart': 'ControlCommand',
#   'attributes': {'lockDoor': {'score': 1,
#     'counterpart': ('LockDoor', 'ControlCommand')},
#    'turnOnHeating': {'score': 1,
#     'counterpart': ('TurnOnHeating', 'ControlCommand')}}},
#                  # checked above
#  'CommandStatus': {'score': 1,
#   'counterpart': 'Status',
#   'attributes': {'Requested': {'score': 1,
#     'counterpart': ('Requested', 'Status')},
#    'Completed': {'score': 1, 'counterpart': ('Completed', 'Status')},
#    'Failed': {'score': 1, 'counterpart': ('Failed', 'Status')}}},
#                  # checked above
#  'RuleStatus': {'score': 1,
#   'counterpart': 'RuleStatus',
#   'attributes': {'created': {'score': 1,
#     'counterpart': ('Created', 'RuleStatus')},
#    'edited': {'score': 1, 'counterpart': ('Edited', 'RuleStatus')},
#    'activated': {'score': 1, 'counterpart': ('Activated', 'RuleStatus')},
#    'deactivated': {'score': 1, 'counterpart': ('Deactivated', 'RuleStatus')}}},
#                  # checked above
#  'BinaryOp': {'score': 0,
#   'counterpart': None,
#   'attributes': {'AND': {'score': 0, 'counterpart': None},
#    'OR': {'score': 0, 'counterpart': None}}},
#                  # checked above
#  'SHAS': {'score': 1, 'counterpart': 'SHAS', 'attributes': {}},
#                  # checked above
#  'SmartHome': {'score': 1, 'counterpart': 'SmartHome', 'attributes': {}},
#                  # checked above
#  'User': {'score': 1,
#   'counterpart': 'User',
#   'attributes': {'string name': {'score': 0,
#     'counterpart': None}}},
#                  # checked above
#  'Address': {'score': 0,
#   'counterpart': None,
#   'attributes': {'string city': {'score': 0.5,
#     'counterpart': ('string address', 'SmartHome')},
#    'string postalCode': {'score': 0, 'counterpart': None},
#    'string street': {'score': 0, 'counterpart': None},
#    'string aptNumber': {'score': 0, 'counterpart': None}}},
#                  # checked above
#  'Room': {'score': 1, 'counterpart': 'Room', 'attributes': {}},
#                  # checked above
#  'abstract Device': {'score': 0.5,
#   'counterpart': 'Device',
#   'attributes': {'DeviceStatus deviceStatus': {'score': 0.5,
#     'counterpart': ('DeviceStatus deviceStatus', 'ChangeInState')},
#    'int deviceID': {'score': 1,
#     'counterpart': ('string deviceIdentifier', 'Device')}}},
#                  # checked above
#  'SensorDevice': {'score': 1, 'counterpart': 'SensorDevice', 'attributes': {}},
#                  # checked above
#  'ActuatorDevice': {'score': 1,
#   'counterpart': 'ActuatorDevice',
#   'attributes': {}},
#                  # checked above
#  'ActivityLog': {'score': 1, 'counterpart': 'ActivityLog', 'attributes': {}},
#                  # checked above
#  'abstract RuntimeElement': {'score': 0,
#   'counterpart': None,
#   'attributes': {'time timestamp': {'score': 0.5,
#     'counterpart': ('time timeStamp', 'SensorReading')}}},
#                  # checked above
#  'SensorReading': {'score': 1,
#   'counterpart': 'SensorReading',
#   'attributes': {'double value': {'score': 1,
#     'counterpart': ('float measuredValue', 'SensorReading')}}},
#                   # checked above
#  'ControlCommand': {'score': 1,
#   'counterpart': 'ActuatorCommand',
#   'attributes': {'CommandType commandType': {'score': 1,
#     'counterpart': ('ControlCommand controlCommand', 'ActuatorCommand')},
#    'CommandStatus commandStatus': {'score': 1,
#     'counterpart': ('Status status', 'ActuatorCommand')}}},
#                   # checked above
#  'AlertRule': {'score': 1,
#   'counterpart': 'AutomationRule',
#   'attributes': {'RuleStatus ruleStatus': {'score': 1,
#     'counterpart': ('RuleStatus ruleStatus', 'AutomationRule')}}},
#                   # checked above
#  'abstract BooleanExpression': {'score': 0.5,
#   'counterpart': 'Precondition',
#   'attributes': {}},
#                   # checked above
#  'RelationalTerm': {'score': 1,
#   'counterpart': 'RelationalTerm',
#   'attributes': {}},
#                   # checked above
#  'NotExpression': {'score': 0, 'counterpart': None, 'attributes': {}},
#                   # checked above
#  'BinaryExpression': {'score': 0,
#   'counterpart': None,
#   'attributes': {'BinaryOp binaryOp': {'score': 0, 'counterpart': None}}},
#                   # checked above
#  'CommandSequence': {'score': 1, 'counterpart': 'Action', 'attributes': {}}}
#  # checked above

# %%
# stu_cls_human = {'DeviceStatus': {'score': 1,
#   'counterpart': 'DeviceStatus',
#   'attributes': {'Activated': {'score': 1,
#     'counterpart': ('Activated', 'DeviceStatus')},
#    'Deactivated': {'score': 1,
#     'counterpart': ('Deactivated', 'DeviceStatus')}}},
#                   # checked above
#  'ControlCommand': {'score': 1,
#   'counterpart': 'CommandType',
#   'attributes': {'LockDoor': {'score': 1,
#     'counterpart': ('lockDoor', 'CommandType')},
#    'TurnOnHeating': {'score': 1,
#     'counterpart': ('turnOnHeating', 'CommandType')}}},
#                   # checked above
#  'Status': {'score': 1,
#   'counterpart': 'CommandStatus',
#   'attributes': {'Requested': {'score': 1,
#     'counterpart': ('Requested', 'CommandStatus')},
#    'Completed': {'score': 1, 'counterpart': ('Completed', 'CommandStatus')},
#    'Failed': {'score': 1, 'counterpart': ('Failed', 'CommandStatus')}}},
#                   # checked above
#  'RuleStatus': {'score': 1,
#   'counterpart': 'RuleStatus',
#   'attributes': {'Created': {'score': 1,
#     'counterpart': ('created', 'RuleStatus')},
#    'Edited': {'score': 1, 'counterpart': ('edited', 'RuleStatus')},
#    'Activated': {'score': 1, 'counterpart': ('activated', 'RuleStatus')},
#    'Deactivated': {'score': 1, 'counterpart': ('deactivated', 'RuleStatus')}}},
#                   # checked above

#  'TypeOfActuator': {'score': 0,
#   'counterpart': None,
#   'attributes': {'LightController': {'score': 0, 'counterpart': None},
#    'LockController': {'score': 0, 'counterpart': None}}},
#                   # checked above
#  'TypeOfSensor': {'score': 0,
#   'counterpart': None,
#   'attributes': {'TemperatureSensor': {'score': 0, 'counterpart': None},
#    'MovementSensor': {'score': 0, 'counterpart': None}}},
#                   # checked above
#  'SHAS': {'score': 1, 'counterpart': 'SHAS', 'attributes': {}},
#                   # checked above
#  'SmartHome': {'score': 1,
#   'counterpart': 'SmartHome',
#   'attributes': {'string address': {'score': 0.5,
#     'counterpart': ('string city', 'Address')}}},
#                   # checked above
#  'User': {'score': 1, 'counterpart': 'User', 'attributes': {}},
#                   # checked above
#  'Room': {'score': 1, 'counterpart': 'Room', 'attributes': {}},
#                   # checked above
#  'Device': {'score': 0.5,
#   'counterpart': 'abstract Device',
#   'attributes': {'string deviceIdentifier': {'score': 1,
#     'counterpart': ('int deviceID', 'abstract Device')}}},
#                   # checked above
#  'SensorDevice': {'score': 1,
#   'counterpart': 'SensorDevice',
#   'attributes': {'TypeOfSensor typeOfSensor': {'score': 0,
#     'counterpart': None}}},
#                   # checked above
#  'ActuatorDevice': {'score': 1,
#   'counterpart': 'ActuatorDevice',
#   'attributes': {'TypeOfActuator typeOfActuator': {'score': 0,
#     'counterpart': None}}},
#                   # checked above
#  'ActivityLog': {'score': 1, 'counterpart': 'ActivityLog', 'attributes': {}},
#                   # checked above
#  'SensorReading': {'score': 1,
#   'counterpart': 'SensorReading',
#   'attributes': {'float measuredValue': {'score': 1,
#     'counterpart': ('double value', 'SensorReading')},
#    'time timeStamp': {'score': 0.5, 'counterpart': ('time timestamp', 'abstract RuntimeElement')}}},
#                   # checked above
#  'ActuatorCommand': {'score': 1,
#   'counterpart': 'ControlCommand',
#   'attributes': {'ControlCommand controlCommand': {'score': 1,
#     'counterpart': ('CommandType commandType', 'ControlCommand')},
#    'Time timeStamp': {'score': 0, 'counterpart': None},
#    'Status status': {'score': 1,
#     'counterpart': ('CommandStatus commandStatus', 'ControlCommand')}}},
#                  # checked above
#  'AutomationRule': {'score': 1,
#   'counterpart': 'AlertRule',
#   'attributes': {'RuleStatus ruleStatus': {'score': 1,
#     'counterpart': ('RuleStatus ruleStatus', 'AlertRule')},
#    'Time timeStamp': {'score': 0,
#     'counterpart': None}}},
#                  # checked above
#  'Precondition': {'score': 0.5,
#   'counterpart': 'abstract BooleanExpression',
#   'attributes': {}},
#                  # checked above
#  'RelationalTerm': {'score': 1,
#   'counterpart': 'RelationalTerm',
#   'attributes': {}},
#                  # checked above
#  'Action': {'score': 1, 'counterpart': 'CommandSequence', 'attributes': {}},
#                  # checked above
#  'InfrastructureMap': {'score': 0, 'counterpart': None, 'attributes': {}},
#                  # checked above
#  'ChangeInState': {'score': 0,
#   'counterpart': None,
#   'attributes': {'DeviceStatus deviceStatus': {'score': 0.5,
#     'counterpart': ('DeviceStatus deviceStatus', 'abstract Device')}}},
#                  # checked above
#  'Owner': {'score': 0, 'counterpart': None, 'attributes': {}},
#                  # checked above
#  'SeparationWord': {'score': 0,
#   'counterpart': None,
#   'attributes': {'String word': {'score': 0,
#     'counterpart': None}}}}
#     # checked above

# %% [markdown]
# ### Relationship

# %%
# ref_rel_human = [{'dsl': '1 SHAS contain * SmartHome', 'score': 0, 'counterpart': None},
#  {'dsl': '1 SHAS contain * User',
#   'score': 1,
#   'counterpart': '1 SHAS contain * User'},
#                  # checked above
#  {'dsl': '1 SmartHome contain 0..1 Address', 'score': 0, 'counterpart': None},
#                  # checked above
#  {'dsl': '1 SmartHome contain * Room',
#   'score': 0.5,
#   'counterpart': '* Room associate 1 SmartHome'},
#                  # checked above
#  {'dsl': '1 SmartHome contain 0..1 ActivityLog',
#   'score': 0,
#   'counterpart': None},
#                   # checked above
#  {'dsl': '* SmartHome associate * User', 'score': 0, 'counterpart': None},
#                   # checked above
#  {'dsl': '1 Room contain * SensorDevice', 'score': 0, 'counterpart': None},
#                    # checked above
#  {'dsl': '1 Room contain * ActuatorDevice', 'score': 0, 'counterpart': None},
#                  # checked above
#  {'dsl': '1 ActivityLog contain * SensorReading',
#   'score': 0.5,
#   'counterpart': '1 ActivityLog associate * SensorReading'},
#                  # checked above
#  {'dsl': '1 ActivityLog contain * ControlCommand',
#   'score': 0.5,
#   'counterpart': '1 ActivityLog associate * ActuatorCommand'},
#                  # checked above
#  {'dsl': '* SensorReading associate 1 SensorDevice',
#   'score': 0.5,
#   'counterpart': '1 SensorDevice contain * SensorReading'},
#                  # checked above
#  {'dsl': '* ControlCommand associate 1 ActuatorDevice',
#   'score': 0.5,
#   'counterpart': '1 ActuatorDevice contain * ActuatorCommand'},
#                  # checked above
#  {'dsl': '1 AlertRule contain 0..1 BooleanExpression',
#   'score': 0.5,
#   'counterpart': '1..* AutomationRule contain 1..* Precondition'},
#                   # checked above
#  {'dsl': '1 AlertRule contain * CommandSequence',
#   'score': 0.5,
#   'counterpart': '1..* AutomationRule contain 1..* Action'},
#                  # checked above
#  {'dsl': '* RelationalTerm associate 0..1  Room',
#   'score': 0,
#   'counterpart': None},
#                  # checked above
#  {'dsl': '* RelationalTerm associate 0..1  Device',
#   'score': 0,
#   'counterpart': None},
#                  # checked above
#  {'dsl': '* RelationalTerm associate 0..1  RuntimeElement',
#   'score': 0,
#   'counterpart': None},
#                  # checked above
#  {'dsl': '0..1 NotExpression associate 1 BooleanExpression',
#   'score': 0,
#   'counterpart': None},
#  {'dsl': '0..1 BinaryExpression associate 1 BooleanExpression',
#   'score': 0,
#   'counterpart': None},
#  {'dsl': '0..1 BinaryExpression associate 1 BooleanExpression',
#   'score': 0,
#   'counterpart': None},
#  {'dsl': '* CommandSequence associate 0..1 CommandSequence',
#   'score': 0,
#   'counterpart': None},
#  {'dsl': '1 CommandSequence contain 0..1 ControlCommand',
#   'score': 0.5,
#   'counterpart': '* Action associate 1..* ActuatorCommand'},
#  {'dsl': 'SensorReading inherit RuntimeElement',
#   'score': 0,
#   'counterpart': None},
#  {'dsl': 'ControlCommand inherit RuntimeElement',
#   'score': 0,
#   'counterpart': None},
#  {'dsl': 'NotExpression inherit BooleanExpression',
#   'score': 0,
#   'counterpart': None},
#  {'dsl': 'BinaryExpression inherit BooleanExpression',
#   'score': 0,
#   'counterpart': None},
#  {'dsl': 'RelationalTerm inherit BooleanExpression',
#   'score': 0,
#   'counterpart': None},
#  {'dsl': 'SensorDevice inherit Device',
#   'score': 1,
#   'counterpart': 'SensorDevice inherit Device'},
#                  # checked above
#  {'dsl': 'ActuatorDevice inherit Device',
#   'score': 1,
#   'counterpart': 'ActuatorDevice inherit Device'}]
#   # checked above

# %%
# stu_rel_human = [{'dsl': '1 SHAS contain * User',
#   'score': 1,
#   'counterpart': '1 SHAS contain * User'},
#                    # checked above
#  {'dsl': '* Room associate 1 SmartHome',
#   'score': 0.5,
#   'counterpart': '1 SmartHome contain * Room'},
#                    # checked above
#  {'dsl': '1 SHAS contain 1 ActivityLog', 'score': 0, 'counterpart': None},
#                    # checked above
#  {'dsl': '* Device assocaite 1 Room', 'score': 0, 'counterpart': None},
#                    # checked above
#  {'dsl': '1 ActivityLog associate * SensorReading',
#   'score': 0.5,
#   'counterpart': '1 ActivityLog contain * SensorReading'},
#                    # checked above
#  {'dsl': '1 ActivityLog associate * ActuatorCommand',
#   'score': 0.5,
#   'counterpart': '1 ActivityLog contain * ControlCommand'},
#                    # checked above
#  {'dsl': '1 SensorDevice contain * SensorReading',
#   'score': 0.5,
#   'counterpart': '* SensorReading associate 1 SensorDevice'},
#                    # checked above
#  {'dsl': '1 ActuatorDevice contain * ActuatorCommand',
#   'score': 0.5,
#   'counterpart': '* ControlCommand associate 1 ActuatorDevice'},
#                    # checked above
#  {'dsl': '1..* AutomationRule contain 1..* Precondition',
#   'score': 0.5,
#   'counterpart': '1 AlertRule contain 0..1 BooleanExpression'},
#                    # checked above
#  {'dsl': '1..* AutomationRule contain 1..* Action',
#   'score': 0.5,
#   'counterpart': '1 AlertRule contain * CommandSequence'},
#                    # checked above
#  {'dsl': '* Action associate 1..* ActuatorCommand',
#   'score': 0.5,
#   'counterpart': '1 CommandSequence contain 0..1 ControlCommand'},
#                    # checked above
#  {'dsl': 'SensorDevice inherit Device',
#   'score': 1,
#   'counterpart': 'SensorDevice inherit Device'},
#                    # checked above
#  {'dsl': 'ActuatorDevice inherit Device',
#   'score': 1,
#   'counterpart': 'ActuatorDevice inherit Device'},
#                    # checked above
#  {'dsl': 'Device inherit RelationalTerm', 'score': 0, 'counterpart': None},
#  {'dsl': 'Room inherit RelationalTerm', 'score': 0, 'counterpart': None},
#  {'dsl': 'User inherit Owner', 'score': 0, 'counterpart': None},
#  {'dsl': '1 SHAS contain 1 InfrastructureMap',
#   'score': 0,
#   'counterpart': None},
#  {'dsl': 'SensorReading inherit RelationalTerm',
#   'score': 0,
#   'counterpart': None},
#  {'dsl': 'ActuatorCommand inherit RelationalTerm',
#   'score': 0,
#   'counterpart': None},
#  {'dsl': '* ChangeInState associate 1 Device',
#   'score': 0,
#   'counterpart': None},
#  {'dsl': '* ChangeInState associate 1 InfrastructureMap',
#   'score': 0,
#   'counterpart': None},
#  {'dsl': '* AutomationRule associate * AutomationRule',
#   'score': 0,
#   'counterpart': None},
#  {'dsl': '1 Owner associate * AutomationRule',
#   'score': 0,
#   'counterpart': None},
#  {'dsl': '* Owner associate * SmartHome', 'score': 0, 'counterpart': None},
#  {'dsl': '* Precondition associate * RelationalTerm',
#   'score': 0,
#   'counterpart': None},
#  {'dsl': '1..* SeparationWord associate * Precondition',
#   'score': 0,
#   'counterpart': None}]
#     # checked above

# %% [markdown]
# ### Save to disk

# %%
# # # import pickle


# with open(student_dir + 'human_grade.pkl', 'wb') as outp:
#     g2 = HumanEvaluation(ref_cls_human, stu_cls_human, ref_rel_human, stu_rel_human)
#     pickle.dump(g2, outp, pickle.HIGHEST_PROTOCOL)


# %% [markdown]
# ### Comparsion

# %%
algo_human = {}
algo_human["class"] = {"precision": 0, "recall": 0, "f1": 0}
algo_human["attribute"] = {"precision": 0, "recall": 0, "f1": 0}
algo_human["relationship"] = {"precision": 0, "recall": 0, "f1": 0}

# %% [markdown]
# #### Class


# %%
def exist_mapping(mappings, one_mapping):
    for m in mappings:
        if m[0] == one_mapping[0] and m[1] == one_mapping[1]:
            return True  # already exist
    return False


# %%
# get human matching first:

tmp = group.ref_cls
human_mappings = []
for key in tmp:
    # print(tmp[key])
    human_mappings.append((key, tmp[key]["counterpart"], tmp[key]["score"]))

tmp = group.stu_cls
for key in tmp:
    # print(tmp[key])

    # reserve the order
    matching = (tmp[key]["counterpart"], key, tmp[key]["score"])

    if not exist_mapping(human_mappings, matching):
        human_mappings.append(matching)

# %%
# compare performance
# algo matching
grader.ref.cls_atr

tmp = grader.ref.cls_atr
EMB_mappings = []
for key in tmp:
    # print(tmp[key])
    EMB_mappings.append((key, tmp[key]["counterpart"], tmp[key]["score"]))

tmp = grader.stu.cls_atr

for key in tmp:
    # print(tmp[key])
    matching = (tmp[key]["counterpart"], key, tmp[key]["score"])

    if not exist_mapping(EMB_mappings, matching):
        EMB_mappings.append(matching)

# %% [markdown]
# ##### Start Evaluation

# %%
# TP/FP/TN/FN
TP = []
FP = []
TN = []
FN = []


def check_TP_TN(map_human, map_algo):
    if (
        map_human[0] == map_algo[0]
        and map_human[1] == map_algo[1]
        and not (None in map_human)
    ):
        return "TP"
    elif (
        map_human[0] == map_algo[0]
        and map_human[1] == map_algo[1]
        and (None in map_human)
    ):
        return "TN"
    else:
        return "NA"


human_mappings_dict = {}
for i in human_mappings:
    human_mappings_dict[i] = False  # not mapped
EMB_mappings_dict = {}
for i in EMB_mappings:
    EMB_mappings_dict[i] = False  # not mapped

# filter out TP or TN first
for i in human_mappings:
    mappinged = False
    if not mappinged:
        for j in EMB_mappings:
            ans = check_TP_TN(i, j)
            if ans == "NA":
                continue
            elif ans == "TP":
                score = 1 if i[2] == j[2] else 0.5
                TP.append((i, j, score))
                human_mappings_dict[i] = True
                EMB_mappings_dict[j] = True
            elif ans == "TN":
                score = 1 if i[2] == j[2] else 0.5
                TN.append((i, j, score))
                human_mappings_dict[i] = True
                EMB_mappings_dict[j] = True


# %%
def find_mapping_with_cls(mapping_dict, mapping, pos):
    # position = 0 or 1
    for i in mapping_dict:
        if i[pos] == mapping[pos]:
            return i
    print("no mapping is found with", mapping, pos)
    return None


# %%
EMB_mappings_dict

# %%
human_mappings_dict

for i in human_mappings_dict:
    if human_mappings_dict[i]:
        continue  # if mapped, ignore

        # i[0] is human pair
    elif i[0] is not None:
        mapping = find_mapping_with_cls(EMB_mappings_dict, i, 0)  # generated pair
        if i[1] is not None and mapping[1] is not None:  # a b	// a c	0	FP
            FP.append((i, mapping))
            human_mappings_dict[i] = True
            EMB_mappings_dict[mapping] = True

        elif i[1] is not None and mapping[1] is None:  # a b	// a None	0	FN
            FN.append((i, mapping))
            human_mappings_dict[i] = True
            EMB_mappings_dict[mapping] = True

        elif i[1] is None and mapping[1] is not None:  # a None // a b	0	FP
            FP.append((i, mapping))
            human_mappings_dict[i] = True
            EMB_mappings_dict[mapping] = True

    elif i[1] is not None:
        mapping = find_mapping_with_cls(EMB_mappings_dict, i, 1)  # generated pair
        if i[0] is None and mapping[0] is not None:  # none a //	b a 	0	FP
            FP.append((i, mapping))
            human_mappings_dict[i] = True
            EMB_mappings_dict[mapping] = True

        elif i[0] is not None and mapping[0] is None:  # b a	// none a  	0	FN
            FN.append((i, mapping))
            human_mappings_dict[i] = True
            EMB_mappings_dict[mapping] = True

        elif i[0] is not None and mapping[0] is not None:  # c a	// b a  0	FP
            FP.append((i, mapping))
            human_mappings_dict[i] = True
            EMB_mappings_dict[mapping] = True


# %%
EMB_mappings_dict

for i in EMB_mappings_dict:
    if EMB_mappings_dict[i]:
        continue  # if mapped, ignore

        # i[0] is generaeted pair
    elif i[0] is not None:
        mapping = find_mapping_with_cls(human_mappings_dict, i, 0)  # human result
        if i[1] is not None and mapping[1] is not None:  # a b	// a c	0	FP
            FP.append((mapping, i))
            human_mappings_dict[mapping] = True
            EMB_mappings_dict[i] = True

        elif mapping[1] is not None and i[1] is None:  # a b	// a None	0	FN
            FN.append((mapping, i))
            human_mappings_dict[mapping] = True
            EMB_mappings_dict[i] = True

        elif mapping[1] is None and i[1] is not None:  # a None // a b	0	FP
            FP.append((mapping, i))
            human_mappings_dict[mapping] = True
            EMB_mappings_dict[i] = True

    elif i[1] is not None:
        mapping = find_mapping_with_cls(human_mappings_dict, i, 1)
        if mapping[0] is not None and i[0] is None:  # b a //	none a 	0	FN
            FN.append((i, mapping))
            human_mappings_dict[mapping] = True
            EMB_mappings_dict[i] = True

        elif mapping[0] is None and i[0] is not None:  # none a //	b a  	0	FP
            FP.append((i, mapping))
            human_mappings_dict[mapping] = True
            EMB_mappings_dict[i] = True

        elif mapping[0] is not None and i[0] is not None:  # c a	// b a  0	FP
            FP.append((i, mapping))
            human_mappings_dict[mapping] = True
            EMB_mappings_dict[i] = True

# %%
EMB_mappings_dict

# %%
# precision = TP /(TP + FP)
# recall = TP /(TP + FN)

tp = 0

for i in TP:
    tp += i[2]

print("precision:", tp / (len(TP) + len(FP)))
print("recall:", tp / (len(TP) + len(FN)))

p = tp / (len(TP) + len(FP))
r = tp / (len(TP) + len(FN))

algo_human["class"]["precision"] = p
algo_human["class"]["recall"] = r

algo_human["class"]["f1"] = 2 * p * r / (p + r)


# %% [markdown]
# #### Attribute

# %%
# algo matching

tmp = group.ref_cls
human_mappings = []
for cls in tmp:  # cls
    for attr in tmp[cls]["attributes"]:  # attributes
        # print(cls, attr)

        human_mappings.append(
            (
                (attr, cls),
                tmp[cls]["attributes"][attr]["counterpart"],
                tmp[cls]["attributes"][attr]["score"],
            )
        )


tmp = group.stu_cls
for cls in tmp:
    # print(tmp[key])
    for attr in tmp[cls]["attributes"]:  # attributes
        # order of the elements
        matching = (
            tmp[cls]["attributes"][attr]["counterpart"],
            (attr, cls),
            tmp[cls]["attributes"][attr]["score"],
        )

        if not exist_mapping(human_mappings, matching):
            # print(matching)
            human_mappings.append(matching)

# %%
# compare performance
# algo matching
grader.ref.cls_atr

tmp = grader.ref.cls_atr
EMB_mappings = []
for cls in tmp:
    # print(tmp[key])
    for attr in tmp[cls]["attributes"]:
        EMB_mappings.append(
            (
                (attr, cls),
                tmp[cls]["attributes"][attr]["counterpart"],
                tmp[cls]["attributes"][attr]["score"],
            )
        )

tmp = grader.stu.cls_atr

for cls in tmp:
    # print(tmp[key])
    for attr in tmp[cls]["attributes"]:
        matching = (
            tmp[cls]["attributes"][attr]["counterpart"],
            (attr, cls),
            tmp[cls]["attributes"][attr]["score"],
        )
        # if "LightController" in str(matching):
        #   print(matching)
        if not exist_mapping(EMB_mappings, matching):
            EMB_mappings.append(matching)

# %%
# TP/FP/TN/FN
TP = []
FP = []
TN = []
FN = []


def check_TP_TN(map_human, map_algo):
    if (
        map_human[0] == map_algo[0]
        and map_human[1] == map_algo[1]
        and not (None in map_human)
    ):
        return "TP"
    elif (
        map_human[0] == map_algo[0]
        and map_human[1] == map_algo[1]
        and (None in map_human)
    ):
        return "TN"
    else:
        return "NA"


human_mappings_dict = {}
for i in human_mappings:
    human_mappings_dict[i] = False  # not mapped
EMB_mappings_dict = {}
for i in EMB_mappings:
    EMB_mappings_dict[i] = False  # not mapped

# filter out TP or TN first
for i in human_mappings:
    mappinged = False
    if not mappinged:
        for j in EMB_mappings:
            ans = check_TP_TN(i, j)
            if ans == "NA":
                continue
            elif ans == "TP":
                score = 1 if i[2] == j[2] else 0.5
                TP.append((i, j, score))
                human_mappings_dict[i] = True
                EMB_mappings_dict[j] = True
            elif ans == "TN":
                score = 1 if i[2] == j[2] else 0.5
                TN.append((i, j, score))
                human_mappings_dict[i] = True
                EMB_mappings_dict[j] = True


# %%
human_mappings_dict

for i in human_mappings_dict:
    if human_mappings_dict[i]:
        continue  # if mapped, ignore

        # i[0] is human pair
    elif i[0] is not None:
        mapping = find_mapping_with_cls(EMB_mappings_dict, i, 0)  # generated pair

        # print(i, mapping)

        if i[1] is not None and mapping[1] is not None:  # a b	// a c	0	FP
            FP.append((i, mapping))
            human_mappings_dict[i] = True
            EMB_mappings_dict[mapping] = True

        elif i[1] is not None and mapping[1] is None:  # a b	// a None	0	FN
            FN.append((i, mapping))
            human_mappings_dict[i] = True
            EMB_mappings_dict[mapping] = True

        elif i[1] is None and mapping[1] is not None:  # a None // a b	0	FP
            FP.append((i, mapping))
            human_mappings_dict[i] = True
            EMB_mappings_dict[mapping] = True

    elif i[1] is not None:
        mapping = find_mapping_with_cls(EMB_mappings_dict, i, 1)  # generated pair
        # print(i)
        # print(mapping)
        if i[0] is None and mapping[0] is not None:  # none a //	b a 	0	FP
            FP.append((i, mapping))
            human_mappings_dict[i] = True
            EMB_mappings_dict[mapping] = True

        elif i[0] is not None and mapping[0] is None:  # b a	// none a  	0	FN
            FN.append((i, mapping))
            human_mappings_dict[i] = True
            EMB_mappings_dict[mapping] = True

        elif i[0] is not None and mapping[0] is not None:  # c a	// b a  0	FP
            FP.append((i, mapping))
            human_mappings_dict[i] = True
            EMB_mappings_dict[mapping] = True


# %%
EMB_mappings_dict

for i in EMB_mappings_dict:
    if EMB_mappings_dict[i]:
        continue  # if mapped, ignore

        # i[0] is generaeted pair
    elif i[0] is not None:
        mapping = find_mapping_with_cls(human_mappings_dict, i, 0)  # human result
        if i[1] is not None and mapping[1] is not None:  # a b	// a c	0	FP
            FP.append((mapping, i))
            human_mappings_dict[mapping] = True
            EMB_mappings_dict[i] = True

        elif mapping[1] is not None and i[1] is None:  # a b	// a None	0	FN
            FN.append((mapping, i))
            human_mappings_dict[mapping] = True
            EMB_mappings_dict[i] = True

        elif mapping[1] is None and i[1] is not None:  # a None // a b	0	FP
            FP.append((mapping, i))
            human_mappings_dict[mapping] = True
            EMB_mappings_dict[i] = True

    elif i[1] is not None:
        mapping = find_mapping_with_cls(human_mappings_dict, i, 1)
        if mapping[0] is not None and i[0] is None:  # b a //	none a 	0	FN
            FN.append((i, mapping))
            human_mappings_dict[mapping] = True
            EMB_mappings_dict[i] = True

        elif mapping[0] is None and i[0] is not None:  # none a //	b a  	0	FP
            FP.append((i, mapping))
            human_mappings_dict[mapping] = True
            EMB_mappings_dict[i] = True

        elif mapping[0] is not None and i[0] is not None:  # c a	// b a  0	FP
            FP.append((i, mapping))
            human_mappings_dict[mapping] = True
            EMB_mappings_dict[i] = True

# %%
# precision = TP /(TP + FP)
# recall = TP /(TP + FN)

tp = 0

for i in TP:
    tp += i[2]

print("precision:", tp / (len(TP) + len(FP)))
print("recall:", tp / (len(TP) + len(FN)))

p = tp / (len(TP) + len(FP))
r = tp / (len(TP) + len(FN))

algo_human["attribute"]["precision"] = p
algo_human["attribute"]["recall"] = r

algo_human["attribute"]["f1"] = 2 * p * r / (p + r)

# %% [markdown]
# #### Relationship

# %%
# algo matching

tmp = group.ref_rels

human_mappings = []
for dic in tmp:  # cls
    # cls is a dict

    matching = (dic["dsl"], dic["counterpart"], dic["score"])

    human_mappings.append(matching)


tmp = group.stu_rels
for dic in tmp:
    # order of the elements
    matching = (dic["counterpart"], dic["dsl"], dic["score"])

    if not exist_mapping(human_mappings, matching):
        # print(matching)
        human_mappings.append(matching)

# %%
# compare performance
# algo matching
grader.ref.rel.rels

tmp = grader.ref.rel.rels
EMB_mappings = []
for dic in tmp:  # cls
    # cls is a dict

    matching = (dic["dsl"], dic["counterpart"], dic["score"])
    EMB_mappings.append(matching)

tmp = grader.stu.rel.rels

for dic in tmp:
    # order of the elements
    matching = (dic["counterpart"], dic["dsl"], dic["score"])

    if not exist_mapping(EMB_mappings, matching):
        # print(matching)
        EMB_mappings.append(matching)


# %% [markdown]
# ##### Start evaluation

# %%
# TP/FP/TN/FN
TP = []
FP = []
TN = []
FN = []


def check_TP_TN(map_human, map_algo):
    if (
        map_human[0] == map_algo[0]
        and map_human[1] == map_algo[1]
        and not (None in map_human)
    ):
        return "TP"
    elif (
        map_human[0] == map_algo[0]
        and map_human[1] == map_algo[1]
        and (None in map_human)
    ):
        return "TN"
    else:
        return "NA"


human_mappings_dict = {}
for i in human_mappings:
    human_mappings_dict[i] = False  # not mapped
EMB_mappings_dict = {}
for i in EMB_mappings:
    EMB_mappings_dict[i] = False  # not mapped

# filter out TP or TN first
for i in human_mappings:
    mappinged = False
    if not mappinged:
        for j in EMB_mappings:
            ans = check_TP_TN(i, j)
            if ans == "NA":
                continue
            elif ans == "TP":
                score = 1 if i[2] == j[2] else 0.5
                TP.append((i, j, score))
                human_mappings_dict[i] = True
                EMB_mappings_dict[j] = True
            elif ans == "TN":
                score = 1 if i[2] == j[2] else 0.5
                TN.append((i, j, score))
                human_mappings_dict[i] = True
                EMB_mappings_dict[j] = True


# %%
EMB_mappings_dict

# %%
EMB_mappings_dict

# %%
for i in human_mappings_dict:
    if i[0] == "1 AutomationRule contain * Action":
        print(i)

# %%
human_mappings_dict

for i in human_mappings_dict:
    print(i)
    if human_mappings_dict[i]:
        continue  # if mapped, ignore

        # i[0] is human pair
    elif i[0] is not None:
        mapping = find_mapping_with_cls(EMB_mappings_dict, i, 0)  # generated pair
        if i[1] is not None and mapping[1] is not None:  # a b	// a c	0	FP
            FP.append((i, mapping))
            human_mappings_dict[i] = True
            EMB_mappings_dict[mapping] = True

        elif i[1] is not None and mapping[1] is None:  # a b	// a None	0	FN
            FN.append((i, mapping))
            human_mappings_dict[i] = True
            EMB_mappings_dict[mapping] = True

        elif i[1] is None and mapping[1] is not None:  # a None // a b	0	FP
            FP.append((i, mapping))
            human_mappings_dict[i] = True
            EMB_mappings_dict[mapping] = True

    elif i[1] is not None:
        mapping = find_mapping_with_cls(EMB_mappings_dict, i, 1)  # generated pair
        if i[0] is None and mapping[0] is not None:  # none a //	b a 	0	FP
            FP.append((i, mapping))
            human_mappings_dict[i] = True
            EMB_mappings_dict[mapping] = True

        elif i[0] is not None and mapping[0] is None:  # b a	// none a  	0	FN
            FN.append((i, mapping))
            human_mappings_dict[i] = True
            EMB_mappings_dict[mapping] = True

        elif i[0] is not None and mapping[0] is not None:  # c a	// b a  0	FP
            FP.append((i, mapping))
            human_mappings_dict[i] = True
            EMB_mappings_dict[mapping] = True


# %%
EMB_mappings_dict

for i in EMB_mappings_dict:
    if EMB_mappings_dict[i]:
        continue  # if mapped, ignore

        # i[0] is generaeted pair
    elif i[0] is not None:
        mapping = find_mapping_with_cls(human_mappings_dict, i, 0)  # human result
        if i[1] is not None and mapping[1] is not None:  # a b	// a c	0	FP
            FP.append((mapping, i))
            human_mappings_dict[mapping] = True
            EMB_mappings_dict[i] = True

        elif mapping[1] is not None and i[1] is None:  # a b	// a None	0	FN
            FN.append((mapping, i))
            human_mappings_dict[mapping] = True
            EMB_mappings_dict[i] = True

        elif mapping[1] is None and i[1] is not None:  # a None // a b	0	FP
            FP.append((mapping, i))
            human_mappings_dict[mapping] = True
            EMB_mappings_dict[i] = True

    elif i[1] is not None:
        mapping = find_mapping_with_cls(human_mappings_dict, i, 1)
        if mapping[0] is not None and i[0] is None:  # b a //	none a 	0	FN
            FN.append((i, mapping))
            human_mappings_dict[mapping] = True
            EMB_mappings_dict[i] = True

        elif mapping[0] is None and i[0] is not None:  # none a //	b a  	0	FP
            FP.append((i, mapping))
            human_mappings_dict[mapping] = True
            EMB_mappings_dict[i] = True

        elif mapping[0] is not None and i[0] is not None:  # c a	// b a  0	FP
            FP.append((i, mapping))
            human_mappings_dict[mapping] = True
            EMB_mappings_dict[i] = True

# %%
# precision = TP /(TP + FP)
# recall = TP /(TP + FN)

tp = 0

for i in TP:
    tp += i[2]

print("precision:", tp / (len(TP) + len(FP)))
print("recall:", tp / (len(TP) + len(FN)))

p = tp / (len(TP) + len(FP))
r = tp / (len(TP) + len(FN))

algo_human["relationship"]["precision"] = p
algo_human["relationship"]["recall"] = r

algo_human["relationship"]["f1"] = 2 * p * r / (p + r)


# %%

# as requested in comment

with open(student_out_dir + "algo_evaluation.txt", "w") as file:
    file.write(json.dumps(algo_human))
