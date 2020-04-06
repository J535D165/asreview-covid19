from asreview.datasets import BaseDataSet
from asreview.datasets import BaseDataGroup


class Cord19Dataset(BaseDataSet):
    dataset_id = "cord19"
    authors = ["Allen institute for AI"]
    title = "CORD-19"
    topic = "Covid-19"
    license = "Covid dataset license"
    link = "https://pages.semanticscholar.org/coronavirus-research"
    last_update = "2020-04-03"
    description = "A free dataset on publications on the corona virus."
    img_url = ("https://pages.semanticscholar.org/hs-fs/hubfs/"
               "covid-image.png?width=300&name=covid-image.png")
    link = "https://pages.semanticscholar.org/coronavirus-research"
    year = 2020


class Cord19DatasetV6(Cord19Dataset):
    dataset_id = "cord19-v6"
    title = "CORD-19 v6"
    date = "2020-04-03"
    statistics = {
        "n_papers": 47298,
        "n_missing_titles": 158,
        "n_missing_abstracts": 8250,
    }
    url = ("https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/2020-04-03/metadata.csv")  # noqa
    sha512 = ("5ba3738e603e2b23c403a46fb2620360415ba3419b09b071f5a5ca16a96422aa78a5456cba7abb18279b6510174273694961b72c28006620c7f28571125cfae2")  # noqa


class Cord19DatasetV6_Dec2019(Cord19Dataset):
    dataset_id = "cord19-v6-2020"
    title = "CORD-19 v5 since Dec. 2019"
    last_update = "2020-04-03"
    statistics = {
        "n_papers": 4774,
        "n_missing_titles": 2,
        "n_missing_abstracts": 1103,
    }
    date = "2020-04-05"
    url = ("https://raw.githubusercontent.com/asreview/asreview-covid19/master/datasets/cord19_v6_20191201.csv")  # noqa
    sha512 = ("f3781cbb4e9e190df38c3fe7fa80ba69bf6f9dbafb158e0426dd4604f2f1ba794450679005a38d0f9f1dad0696e2f22b8b086b2d7d08a0f99bb4fd3b0f7ed5d8")  # noqa


class Covid19DataGroup(BaseDataGroup):
    group_id = "covid19"
    description = "A Free dataset on publications on the corona virus."

    def __init__(self):
        super(Covid19DataGroup, self).__init__(
            Cord19DatasetV6(),
            Cord19DatasetV6_Dec2019(),
        )
