from applications.project.src.application.commons.di.containers import \
    ApplicationIoC

main = ApplicationIoC.main()

main[0].run()
