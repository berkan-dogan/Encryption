#include <iostream>
#include <fstream>
#include <string>
#include <ctime>
#include <sstream>
#include <iomanip>

class Logger {
public:
    enum LogLevel {
        INFO,
        WARNING,
        ERROR,
        DEBUG
    };

    Logger(const std::string& filename) {
        logFile.open(filename, std::ios::app);
        if (!logFile.is_open()) {
            std::cerr << "Log dosyası açılırken bir hata oluştu!" << std::endl;
            exit(1); // Hata durumunda çık
        }
    }

    ~Logger() {
        if (logFile.is_open()) {
            logFile.close();
        }
    }

    // Logları hem dosyaya hem de terminale yaz
    void log(LogLevel level, const std::string& message) {
        std::string logMessage = currentDateTime() + " - " + logLevelToString(level) + " - " + message;

        // Dosyaya yaz
        if (logFile.is_open()) {
            logFile << logMessage << std::endl;
        }

        
    }

private:
    std::ofstream logFile;

    std::string currentDateTime() {
        std::time_t now = std::time(0);
        std::tm* localtm = std::localtime(&now);
        std::ostringstream oss;
        oss << std::put_time(localtm, "%Y-%m-%d %H:%M:%S");
        return oss.str();
    }

    std::string logLevelToString(LogLevel level) {
        switch (level) {
            case INFO: return "INFO";
            case WARNING: return "WARNING";
            case ERROR: return "ERROR";
            case DEBUG: return "DEBUG";
            default: return "UNKNOWN";
        }
    }
};

void readLogFile(const std::string& filename) {
    std::ifstream logFile(filename); // Dosyayı okuma modunda aç

    if (!logFile.is_open()) {
        std::cerr << "Dosya açılamadı!" << std::endl;
        return;
    }

    std::string line;
    // Dosya sonuna kadar satır satır oku
    while (std::getline(logFile, line)) {
        std::cout << line << std::endl; // Her satırı ekrana yazdır
    }

    logFile.close(); // Dosyayı kapat
}

int main() {
    Logger logger("app.log");

    logger.log(Logger::INFO, "Uygulama başladı.");
    logger.log(Logger::DEBUG, "Debug mesajı: İşlem devam ediyor.");
    logger.log(Logger::WARNING, "Dikkat: Bu bir uyarıdır.");
    logger.log(Logger::ERROR, "Hata: Bir şeyler ters gitti!");

    
    readLogFile("app.log");

    return 0;
}