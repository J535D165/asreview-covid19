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
    sha512 = ("a6d8e7a4dd3f0194840129b7368fd97354b44a44fc0d06addfc9a27f3c08e19ef88ff568effb92994895353f7e9d771932f354bd619ee2242d4262f7561f41fe")  # noqa


class Cord19DatasetV5_Dec2019(Cord19Dataset):
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
    sha512 = ("390c04b690abff2f824ed837367048308c6573032b2e45301056c3cfa7b04e6ea5b00ebd691e1af2066a820335bea1bdad240df736bd69be0b3c436fca629759")  # noqa


class Covid19DataGroup(BaseDataGroup):
    group_id = "covid19"
    description = "A Free dataset on publications on the corona virus."

    def __init__(self):
        super(Covid19DataGroup, self).__init__(
            Cord19DatasetV6(),
            Cord19DatasetV6_Dec2019(),
        )
