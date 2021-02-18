# mecab-ko-dic

This is a Korean dictionary for the MeCab tokenizer, packaged for use in Python
with [mecab-python3](https://github.com/SamuraiT/mecab-python3) or
[fugashi](https://github.com/polm/fugashi). 


## Should you use this?

We (at Luminoso) think this is probably a better way to find tokens in Korean
words than just splitting the text on spaces would be. We also know that MeCab
wasn't designed for Korean. But it gives us the kind of tokens we need better
than other things we've tried.

One reason we're packaging this is to use it in [wordfreq][], which needs to
have a reasonable set of consistent tokens so it can look up their frequencies,
and already uses MeCab for Japanese.

[wordfreq]: https://github.com/LuminosoInsight/wordfreq

If interoperability with things that already use MeCab is not your goal, you
probably have better options for Korean NLP than this.


## Credits

The dictionary data was created by Yongwoon Lee and Yungho Yu. We've included it
as part of this package under the terms of the Apache License 2.0. The original
dictionary can be found [here][original-dict].

The idea to package a MeCab dictionary as a Python repository, as well as the
code structure for doing so, come from [Paul McCann's ipadic package][ipadic-py].

[original-dict]: https://bitbucket.org/eunjeon/mecab-ko-dic/
[ipadic-py]: https://github.com/polm/ipadic-py


## Usage

To install:

    pip install mecab-ko-dic

To initialize with mecab-python3:

    import MeCab
    import mecab_ko_dic
    tagger = MeCab.Tagger(mecab_ko_dic.MECAB_ARGS)
    print(tagger.parse("안녕하세요세계."))


## License

The data we use, and this code repository itself, are released under the Apache
License 2.0. See the LICENSE.txt file included in this distribution.
