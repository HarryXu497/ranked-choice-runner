from ranked_choice_application import RankedChoiceApplication


def main():
    application = RankedChoiceApplication(
        metadata_filepath="metadata.json",
        threshold=0.5,
        display_delay=2
    )

    application.run()


if __name__ == '__main__':
    main()
