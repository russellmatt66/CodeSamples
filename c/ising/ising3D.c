#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define DIM_X 10
#define DIM_Y 10
#define DIM_Z 10

#define THERMAL_STEP 1000
#define SIM_STEPS 10000

#define TEMP_MIN 3.6
#define TEMP_MAX 5.2
#define TEMP_STEP 0.01

#define OUTPUT_FILE "simulation_results.txt"

// Function Prototypes
double random_uniform();
int random_int(int range);
void flip_spin(int ***lattice, int x, int y, int z, double *energy, double *magnetization, double temp);
void initialize_lattice(int ***lattice, double *energy, double *magnetization);
void run_simulation(int ***lattice, FILE *outfile);

int main() {
    srand(time(NULL));
    int ***lattice = malloc(DIM_Z * sizeof(int **));
    for (int k = 0; k < DIM_Z; k++) {
        lattice[k] = malloc(DIM_Y * sizeof(int *));
        for (int j = 0; j < DIM_Y; j++) {
            lattice[k][j] = malloc(DIM_X * sizeof(int));
        }
    }

    clock_t start, end;
    double cpu_time_used;

    FILE *outfile = fopen(OUTPUT_FILE, "w");
    if (outfile == NULL) {
        fprintf(stderr, "Failed to open output file.\n");
        return EXIT_FAILURE;
    }

    start = clock();
    run_simulation(lattice, outfile);
    end = clock();

    cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("Time taken: %f seconds\n", cpu_time_used);

    // Free memory
    for (int k = 0; k < DIM_Z; k++) {
        for (int j = 0; j < DIM_Y; j++) {
            free(lattice[k][j]);
        }
        free(lattice[k]);
    }
    free(lattice);
    fclose(outfile);

    return EXIT_SUCCESS;
}

double random_uniform() {
    return rand() / (RAND_MAX + 1.0);
}

int random_int(int range) {
    return (int)(random_uniform() * range);
}

void flip_spin(int ***lattice, int x, int y, int z, double *energy, double *magnetization, double temp) {
    int x_minus = (x == 0 ? DIM_X - 1 : x - 1);
    int x_plus = (x == DIM_X - 1 ? 0 : x + 1);
    int y_minus = (y == 0 ? DIM_Y - 1 : y - 1);
    int y_plus = (y == DIM_Y - 1 ? 0 : y + 1);
    int z_minus = (z == 0 ? DIM_Z - 1 : z - 1);
    int z_plus = (z == DIM_Z - 1 ? 0 : z + 1);

    int neighbor_sum = lattice[z][y][x_minus] + lattice[z][y][x_plus] + lattice[z][y_minus][x] + lattice[z][y_plus][x] + lattice[z_minus][y][x] + lattice[z_plus][y][x];
    int delta_E = 2 * lattice[z][y][x] * neighbor_sum;
    int delta_M = -2 * lattice[z][y][x];

    if (delta_E < 0 || (delta_E >= 0 && random_uniform() < exp(-delta_E / temp))) {
        lattice[z][y][x] = -lattice[z][y][x];
        *energy += delta_E;
        *magnetization += delta_M;
    }
}

void initialize_lattice(int ***lattice, double *energy, double *magnetization) {
    for (int x = 0; x < DIM_X; x++) {
        for (int y = 0; y < DIM_Y; y++) {
            for (int z = 0; z < DIM_Z; z++) {
                lattice[z][y][x] = 1;
            }
        }
    }
    *magnetization = DIM_Z * DIM_Y * DIM_X;
    *energy = -3 * *magnetization;
}

void run_simulation(int ***lattice, FILE *outfile) {
    double energy, magnetization, temp, avg_energy, avg_magnet, avg_energy2, avg_magnet2, heat_capacity, susceptibility, order_param;

    for (temp = TEMP_MIN; temp <= TEMP_MAX; temp += TEMP_STEP) {
        printf("%lf\n", temp);
        initialize_lattice(lattice, &energy, &magnetization);

        for (int step = 0; step < THERMAL_STEP; step++) {
            for (int flip_count = 0; flip_count < DIM_Z * DIM_Y * DIM_X; flip_count++) {
                int x = random_int(DIM_X);
                int y = random_int(DIM_Y);
                int z = random_int(DIM_Z);
                flip_spin(lattice, x, y, z, &energy, &magnetization, temp);
            }
        }

        avg_energy = avg_magnet = avg_energy2 = avg_magnet2 = order_param = heat_capacity = susceptibility = 0;
        for (int step = 0; step < SIM_STEPS; step++) {
            for (int flip_count = 0; flip_count < DIM_Z * DIM_Y * DIM_X; flip_count++) {
                int x = random_int(DIM_X);
                int y = random_int(DIM_Y);
                int z = random_int(DIM_Z);
                flip_spin(lattice, x, y, z, &energy, &magnetization, temp);
            }

            avg_energy += energy;
            avg_magnet += magnetization;
            avg_energy2 += energy * energy;
            avg_magnet2 += magnetization * magnetization;
            order_param += fabs(magnetization);
        }

        avg_energy /= SIM_STEPS;
        avg_magnet /= SIM_STEPS;
        avg_energy2 /= SIM_STEPS;
        avg_magnet2 /= SIM_STEPS;
        order_param /= SIM_STEPS;
        order_param /= DIM_Z * DIM_Y * DIM_X;
        heat_capacity = (avg_energy2 - avg_energy * avg_energy) / (temp * temp * DIM_Z * DIM_Y * DIM_X);
        susceptibility = (avg_magnet2 - avg_magnet * avg_magnet) / (temp * DIM_Z * DIM_Y * DIM_X);
        fprintf(outfile, "%lf %lf %lf %lf\n", temp, order_param, heat_capacity, susceptibility);
    }
}
