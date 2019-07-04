from project.app.commons.di.containers import ApplicationIoC


main = ApplicationIoC.main()

main[0].run()
