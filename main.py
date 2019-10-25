import record


def main():
    rec = record.Record()
    audio = rec.record_audio()
    words = rec.split_into_words(audio)
    text = rec.print_list(words, rec.is_numbered)
    print(text)


if __name__ == '__main__':
    main()
