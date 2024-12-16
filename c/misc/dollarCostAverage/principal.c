#include <stdio.h>
#include <stdlib.h>

float P(int n, float base, float ror){
	if (n == 1) return base * ror;
	return (P(n-1, base, ror) + base) * ror;
}

int main(int argc, char* argv[]){
	int num_years = atoi(argv[1]);
	float base = atof(argv[2]);
	float yar = atof(argv[3]);

	float value_yearly = P(num_years, base, yar);

	float mar = 1.0 + (yar - 1.0) / 12;
	int  num_months = 12 * num_years;
	float base_monthly = base / 12;	
	float value_monthly = P(num_months, base_monthly, mar);

	float war = 1.0 + (yar - 1.0) / 52;
	int num_weeks = 52 * num_years;
	float base_weekly = base / 52;
	float value_weekly = P(num_weeks, base_weekly, war);

	float dar = 1.0 + (yar - 1.0) / 365;
	int num_days = 365 * num_years;
	float base_daily = base / 365;
	float value_daily = P(num_days, base_daily, dar);

	printf("Principal after %d years of yearly compounding is $%f\n", num_years, value_yearly);
	printf("Principal after %d months of monthly compounding is $%f\n", num_months, value_monthly);
	printf("Principal after %d weeks of weekly compounding is $%f\n", num_weeks, value_weekly);
	printf("Principal after %d days of daily compounding is $%f\n", num_days, value_daily);
	return 0;
}
