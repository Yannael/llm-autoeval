"""Example script for benchmarking all datasets constituting the MTEB English leaderboard & average scores"""

import logging
import os
import time


from mteb import MTEB
from sentence_transformers import SentenceTransformer

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("main")

TASK_LIST_CLASSIFICATION = [
    "AmazonCounterfactualClassification",
    "AmazonPolarityClassification",
    "AmazonReviewsClassification",
    "Banking77Classification",
    "EmotionClassification",
    "ImdbClassification",
    "MassiveIntentClassification",
    "MassiveScenarioClassification",
    "MTOPDomainClassification",
    "MTOPIntentClassification",
    "ToxicConversationsClassification",
    "TweetSentimentExtractionClassification",
]

TASK_LIST_CLUSTERING = [
    "ArxivClusteringP2P",
    "ArxivClusteringS2S",
    "BiorxivClusteringP2P",
    "BiorxivClusteringS2S",
    "MedrxivClusteringP2P",
    "MedrxivClusteringS2S",
    "RedditClustering",
    "RedditClusteringP2P",
    "StackExchangeClustering",
    "StackExchangeClusteringP2P",
    "TwentyNewsgroupsClustering",
]

TASK_LIST_PAIR_CLASSIFICATION = [
    "SprintDuplicateQuestions",
    "TwitterSemEval2015",
    "TwitterURLCorpus",
]

TASK_LIST_RERANKING = [
    "AskUbuntuDupQuestions",
    #"MindSmallReranking",
    "SciDocsRR",
    "StackOverflowDupQuestions",
]

TASK_LIST_RETRIEVAL = [
    #"ArguAna",
    #"ClimateFEVER",
    #"CQADupstackAndroidRetrieval",
    #"CQADupstackEnglishRetrieval",
    #"CQADupstackGamingRetrieval",
    #"CQADupstackGisRetrieval",
    #"CQADupstackMathematicaRetrieval",
    #"CQADupstackPhysicsRetrieval",
    #"CQADupstackProgrammersRetrieval",
    #"CQADupstackStatsRetrieval",
    #"CQADupstackTexRetrieval",
    #"CQADupstackUnixRetrieval",
    #"CQADupstackWebmastersRetrieval",
    #"CQADupstackWordpressRetrieval",
    #"DBPedia",
    "FEVER",
    "FiQA2018",
    "HotpotQA",
    "MSMARCO",
    "NFCorpus",
    "NQ",
    "QuoraRetrieval",
    "SCIDOCS",
    "SciFact",
    "Touche2020",
    "TRECCOVID",
]

TASK_LIST_STS = [
    "BIOSSES",
    "SICK-R",
    "STS12",
    "STS13",
    "STS14",
    "STS15",
    "STS16",
    "STS17",
    "STS22",
    "STSBenchmark",
    "SummEval",
]

TASK_LIST = (
    #TASK_LIST_CLASSIFICATION
    #+ TASK_LIST_CLUSTERING
    #+ TASK_LIST_PAIR_CLASSIFICATION
    #+ TASK_LIST_RERANKING
     TASK_LIST_RETRIEVAL
    + TASK_LIST_STS
)

#TASK_LIST = (["BiorxivClusteringS2S", "BiorxivClusteringP2P"])

model_name = os.getenv("MODEL")
model = SentenceTransformer(model_name)

for task in TASK_LIST:
    logger.info(f"Running task: {task}")
    eval_splits = ["dev"] if task == "MSMARCO" else ["test"]

    start_time=time.time()
    evaluation = MTEB(tasks=[task], task_langs=["en"])  # Remove "en" for running all languages
    evaluation.run(model, output_folder=f"results/{model_name}", eval_splits=eval_splits)
    duration=time.time()-start_time

    with open("durations.txt", "a") as myfile:
        myfile.write(task+" | "+str(duration) + "\n")






