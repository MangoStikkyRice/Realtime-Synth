#include <vector>
#include <cmath>
#include <numeric>

double TWO_PI = 2 * M_PI;

class Oscillator {
    public:
        double sampleRate;
        double frequency;
        double amplitude;
        double phase;
        double increment;

        Oscillator(double sampleRate, double frequency, double amplitude, double phase) {
            this->sampleRate = sampleRate;
            this->frequency = frequency;
            this->amplitude = amplitude;
            this->phase = phase;
            this->increment = TWO_PI * this->frequency / this->sampleRate;
        }

        void process(float* out, int numSamples) {
            for (int i = 0; i < numSamples; i++) {
                this->phase += increment;
                this->phase -= (this->phase >= TWO_PI) * TWO_PI;
                out[i] = static_cast<float>(this->amplitude * sin(this->phase));
            }
        }

        void setFrequency(double frequency) {
            this->frequency = frequency;
            this->increment = TWO_PI * frequency / this->sampleRate;
        }

        void setAmplitude(double amplitude) {
            this->amplitude = amplitude;
        }

        void resetPhase(double phase = 0.0) {
            this->phase = phase;
        }
};