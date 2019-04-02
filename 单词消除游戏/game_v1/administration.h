using namespace std;

class administrator :public individual
{
private:
	void set_question(int role, string player_inf, string  adm_inf, string question);//³öÌâÄ£¿é
public:
	void adm_operation(int role, string player_inf, string  adm_inf, string question);
};