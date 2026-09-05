class Solution {
    public int compress(char[] chars) {

        if(chars.length == 1){
            return 1;
        }

        char[] compress = new char[chars.length];
        int index = 0;

        for(int i = 0; i < chars.length; i++){
            Integer count = 1;

            while(i < chars.length - 1 && chars[i] == chars[i+1]){
                count++;
                i++;
            }

            compress[index++] = chars[i];

            if(count > 1){
                String str = count.toString();

                for(int j = 0; j < str.length(); j++){
                    compress[index++] = str.charAt(j);
                }
            }
        }

        for(int i = 0; i < index; i++){
            chars[i] = compress[i];
        }

        return index;
    }
}

