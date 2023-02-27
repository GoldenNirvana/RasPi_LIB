#include <bits/stdc++.h>

#define rep(i, n) for (int (i) = 0; (i) < (n); ++(i))
#define ll long long
#define vi std::vector<int>
#define vl std::vector<long long>
#define rep1(i, n) for (int (i) = 1; (i) < (n); ++(i))
#define rep1n(i, n) for (int (i) = 1; (i) <= (n); ++(i))
#define pb push_back
#define eb emplace_back
#define each(x, a) for (auto &(x) : (a))
#define cyes std::cout << "YES\n"
#define cno std::cout << "NO\n"
#define stop int stop = 0;

ll next()
{
  ll x;
  std::cin >> x;
  return x;
}

using std::string;
using std::vector;

namespace std
{
  template<typename T, typename Y>
  ostream &operator<<(ostream &out, const pair<T, Y> &pair)
  {
    out << pair.first << ' ' << pair.second << '\n';
    return out;
  }
}

template<typename Container>
void printElements(Container &container, std::ostream &out = std::cout)
{
  std::copy(container.begin(), container.end(), std::ostream_iterator<typename Container::value_type>(out, "  "));
}


void solve()
{
  std::map<int, std::set<int>> map;
  ll n = next();
  vi v;
  v[21]++;
  ll max = 0;
  for (int i = 0; i < n; ++i)
  {
    std::bitset<32> b = next();
    map[b.count()].insert(b.to_ulong());
    for (const auto &item1: map.rbegin()->second)
    {
      int f = item1;
      for (auto j = std::next(map.rbegin()); j != map.rend(); ++j)
      {
        for (const auto &item: j->second)
        {
          if ((f ^ item) > max)
          {
            max = f ^ item;
          }
        }
      }
    }
    std::cout << max << '\n';
  }
}

std::mutex mutex;

void foo()
{
  mutex.lock();
  rep(i, 10000)
  {
    std::cout << i << ' ';
  }
  mutex.unlock();
}

void foo2()
{
  mutex.lock();
  rep(i, 10000)
  {
    std::cout << static_cast<char>(i) << ' ';
  }
  mutex.unlock();
}


struct ListNode
{
  int val;
  ListNode *next;

  ListNode() : val(0), next(nullptr)
  {}

  ListNode(int x) : val(x), next(nullptr)
  {}

  ListNode(int x, ListNode *next) : val(x), next(next)
  {}
};

class Solution
{
public:
  ListNode *reverseList(ListNode *head)
  {
    if (head->next == nullptr)
    {
      return head;
    }
    ListNode *temp;
    while (head->next != nullptr)
    {
      temp = head;
      head = head->next;
      head->next = temp;
    }
    head->next = temp;
    return head;

  }
};


class BasicDevice
{
public:
  virtual void setFreq(int)
  { std::cerr << "err\n"; };

  virtual void read()
  { std::cerr << "err\n"; };
  virtual ~BasicDevice() = default;
  virtual void doSettings() = 0;
};

class WaveGen : public BasicDevice
{
public:
  explicit WaveGen(int hz)
  { this->hz = hz; }

  void setFreq(int f) override
  {
    hz = f;
  }

  void doSettings() override
  {
    std::cout << "doSomeSettingsForWaveGen\n";
  }

  int hz;
};

class Adc : public BasicDevice
{
public:
  explicit Adc(int ch)
  {
    chanel = ch;
  }

  void read() override
  {
    std::cout << "read\n";
  }

  void doSettings() override
  {
    std::cout << "doSomeSettingsForAdc\n";
  }

private:
  int chanel;
};

class Decoder
{
public:
  int a, b, c; // ports
  void enable(int port)
  {
    std::cout << "decoder enable port " << port << '\n';
  }
};


class Controller
{
public:
  std::vector<std::unique_ptr<BasicDevice>> list;

  BasicDevice *operator[](int i)
  {
    decoder.enable(i);
    list[i].get()->doSettings();
    return list[i].get();
  }

private:
  Decoder decoder;
};

std::unique_ptr<BasicDevice> makeWaveGen()
{
  return std::make_unique<Adc>(5);
}

class Solution3
{
public:
  int singleNumber(vector<int> &nums)
  {
    std::map<int, int> mp;
    for (auto x: nums)
    {
      mp[x]++;
    }
    for (auto x: mp)
    {
      if (x.second == 1)
      {
        return x.second;
      }
    }
    return -1;
  }
};

int main()
{
  Controller controller;

  controller.list.push_back(std::make_unique<WaveGen>(2));
  controller.list.push_back(std::make_unique<Adc>(5));
  controller.list.push_back(makeWaveGen());


  controller[0]->setFreq(10000);
  controller[1]->read();
  //controller[0]->read();


  return 0;
}
